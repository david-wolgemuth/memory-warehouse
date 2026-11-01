---
harness: codex
started: 2026-09-30 00:00:00+00:00
tags:
- ai-tooling
- fine-tuning
- economics
- visualization
visibility: public
related:
- ./rag-and-small-company-fine-tuning-economics.md
---


# Visualizing fine-tuning break-even under a Luna-class price target

## User direction

David asked for graphs showing when a regularly retuned model becomes worth its cost, which retraining cadence is affordable, and how model size changes the picture. He suggested line graphs with an intersection point, and asked for a search of how others have visualized the same question. This builds on his existing preference for visual explanations of relationships and trade-offs.

## Existing visual patterns reviewed

- [LLMTCO's cost-versus-volume curve](https://llmtco.com/compare/cost-curve/) shows a rising API line and fixed self-hosting line with a marked crossing. This is the clearest starting form, but a fixed hosting line is only a lower bound until measured capacity and replica scaling are included.
- [The LLM Deploy Cost Calculator](https://github.com/ree2raz/llm-cost-calculator) uses a step-function break-even chart as GPU count jumps. Its README specifically models total (rather than only active) MoE parameters, KV cache, throughput, peak load, and replicas. This is a better production extension once those measurements exist.
- [RightNow AI's inference-cost-truth](https://github.com/RightNow-AI/inference-cost-truth) combines timestamped API/GPU/throughput evidence with a break-even model and names excluded costs such as engineer time, redundancy, and evaluations.
- [Cost-Aware Model Selection for Text Classification](https://arxiv.org/abs/2602.06370) plots quality/cost Pareto trade-offs for fine-tuned encoders and LLM prompting. This suggests that the model-size question needs a quality gate, not merely a price intersection.
- [Inference Engineering Pareto Atlas](https://arxiv.org/abs/2609.17863) plots quality, latency, and cost together using measured anchors plus calibrated simulation, and keeps simulated values identifiable. It reinforces the need to measure throughput and output quality on the actual candidate deployment before treating a dollar crossing as a recommendation.

I did not find an established public chart that directly plots *retuning cadence against rapidly improving Luna-class API price*. The cadence chart here is a derived scenario, not a reproduced result.

## Source data and assumptions for three charts

The Python renderer (unavailable in this public edition) and its SVG charts are stored beside this log: volume (unavailable in this public edition), cadence (unavailable in this public edition), and model size and quality (unavailable in this public edition). Run `python3 logs/2026/09/30/render-fine-tuning-break-even-charts.py` from the Warehouse root to regenerate the SVGs. To make temporary PNGs for Paseo image attachments, pass `--png-dir /tmp/warehouse-finetuning-previews`; that optional path uses the locally installed GdkPixbuf SVG loader. David later clarified that those PNG previews should not be retained in Warehouse; see the [storage correction](./code-rendered-visuals-keep-source-not-png-previews.md).

- [OpenAI's GPT-6 Luna pricing](https://developers.openai.com/api/docs/pricing): Standard $0.10/M input, $0.50/M output; Batch/Flex $0.05/M input, $0.25/M output (short context). The hypothetical request has 1,000 uncached input tokens and 200 *total* output tokens, giving $200 or $100 per million requests respectively. Real reasoning outputs can be much longer.
- [Hugging Face endpoint prices](https://huggingface.co/docs/inference-endpoints/pricing): the illustrative host tiers are $0.80/hour (L4), $1.80/hour (L40S), and $5/hour (H200). The charts charge 730 running hours per month. These are hardware tiers, **not** claims that a particular open model fits, performs, or reaches Luna accuracy on one such GPU.
- A tuning run is **assumed** to cost $200; this is a scenario knob, equivalent to ten hours on eight A100s at [Hugging Face Jobs' $20/hour list price](https://huggingface.co/docs/hub/en/jobs-pricing). Actual jobs and experiment counts vary substantially. Monthly retraining cost is modeled as `$200 × 30 / days_between_runs`.
- Chart 1 uses a 14-day cadence. Monthly hosted cost floors are about $1,013, $1,743, and $4,079 for the three hardware tiers. Against Standard Luna, intersections occur at 5.1M, 8.7M, and 20.4M requests/month; against Batch/Flex, at 10.1M, 17.4M, and 40.8M.
- Chart 2 fixes volume at 10M requests/month. At that volume, L4 hosting falls below Standard Luna at a cadence slower than about 4.2 days, and below Batch/Flex only when slower than about 14.4 days. L40S hosting falls below Standard Luna when slower than about 8.7 days, and never falls below Batch/Flex under these assumptions.
- [Artificial Analysis comparisons](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-luna-vs-qwen3-5-9b), [Qwen3.8 27B comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-qwen3-8-27b), and [Qwen3.8 Flash comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-qwen3-8-flash-next) supply chart 3's current composite index points: Qwen3.5 9B non-reasoning 13; Qwen3.8 27B xhigh 34; Qwen3.8 Flash-Next 180B total/6B active 40; Luna medium 29 and max 37. These are heterogeneous model settings, not tuned variants or a model-size scaling law. The benchmark score does not predict David's task accuracy.

## Reading and limitations

The intersections mean only that a *lower-bound hardware-plus-training bill* equals the listed API bill for the assumed request shape. Every hosted curve is drawn flat to make the first crossover visible; it must become a step function when an actual throughput, latency, peak-load, redundancy, and memory plan determines replica counts. A higher-quality model may use more output tokens per task, shifting its effective cost. Labor, data curation, evaluation, extra training attempts, storage, network, and downtime are omitted. A crossing is therefore a candidate for benchmarking, not proof that tuning pays.

The model-size chart addresses a separate gate: an economical 9B deployment is irrelevant if it misses the quality target; an open-weight model near Luna's broad score can have much larger total stored weights. The meaningful next measurement would be a small set of actual company tasks run through Luna and candidate open models, recording pass rate, total input/output tokens, p95 latency, measured requests per GPU-hour, and the cost of each retuning cycle. Those values can replace the scenario lines with a defensible decision chart.

## Correction: managed fine-tuning of closed models

David clarified that the economics question also concerns fine-tuning a provider's closed model on Bedrock, Google's platform, or Microsoft Foundry. The first three charts model **self-hosted open weights** and their GPU floors; their intersections cannot be transferred to a managed tuned endpoint. The fourth chart (unavailable in this public edition) instead models an API baseline and managed tuning with no fixed GPU hosting bill. The same renderer produces this chart.

The chart uses an **illustrative** $200 per million requests baseline (1,000 input plus 200 output tokens at Luna Standard rates) and $300 of training cost **each month**. It does not claim those are a specific Bedrock, Google, or Foundry tuned-model quote. If tuning leaves token use and price unchanged, the tuned line is a fixed $300 above the base line: volume alone never produces an intersection. If the tuned token rate is 1.5 times the base rate, the difference grows with volume. If tuning reduces billed tokens by 30% at the same per-token rate, savings are $60 per million requests, so $300 monthly retraining breaks even at 5 million requests/month. These lines assume equal task quality; quality improvements or fewer retries need a per-task value model.

Platform evidence checked 2026-09-30:

- [Amazon Bedrock's supported fine-tuning list](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html) includes closed Amazon Nova models and Anthropic Claude 3 Haiku, plus open-weight Meta Llama. It does not imply every Bedrock model can be tuned. [Bedrock's on-demand custom deployment list](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-custom-model-on-demand.html) includes Nova models and Llama 3.3 70B, but not Claude 3 Haiku. [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) states that on-demand custom Nova inference has the same token price as base Nova inference; training tokens and model storage are additional. [AWS's customization job guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit.html) says jobs can take several hours, depending on data, epochs, and batch size.
- [Google's supported tuning list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/tuning) includes closed Gemini 3.5 Flash, Gemini 3.1 Flash-Lite, and Gemini 2.5 models. [Google's pricing page](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) lists Gemini 3.5 Flash training at $10 per million processed training tokens, counted as dataset tokens multiplied by epochs. Ten million dataset tokens for three epochs would cost $300 for that model. The same price page says tuned Gemini 3 inference is 1.5 times the base model rate, whereas older Gemini tuned inference remains at the base rate. Thus a Gemini 3 tuned model must reduce billed usage by more than one-third before it can save inference dollars, even before training cost.
- [Microsoft Foundry's cost guide](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning-cost-management) says standard fine-tuned deployments pay the base token rate **plus $1.70/hour hosting** in its current table; global standard has the same stated hosting fee, developer tier has no hosting fee but lacks an SLA and expires after 24 hours, and provisioned deployments use PTU-hours. At 730 hours, the stated standard hosting fee is about $1,241/month before training or tokens. Microsoft cautions that its guide's numeric prices are examples and points to its price page and commercial agreement for current quotes.

The managed cost equation is `training cost per run × runs per month + deployment/hosting/storage + sum of tuned input and output token charges + evaluation/operations`. Compare it to the *best feasible untuned model* at equal measured quality, not just the tuned model's own base. If the new base drops in price or improves quality, rerun the comparison; the break-even volume rises when the per-task savings shrink. A fast CI/CD training cycle makes retuning operationally possible, but does not by itself create per-request savings.
