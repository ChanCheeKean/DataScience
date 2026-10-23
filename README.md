# DecodeAI

**Decode AI from first principles. No black boxes. No hand-waving.**

This repository is built on a simple belief: you cannot truly master AI by calling `model.fit()`. To understand how modern AI systems actually work, you need to **build them from scratch** — derive the math, implement the algorithms, and watch the gradients flow.

Every notebook in this repository dissects a core AI concept by implementing it from the ground up using raw PyTorch and NumPy. We go from the bias-variance tradeoff all the way to building GPT, LLaMA, DeepSeek, and GRPO — the same algorithm behind DeepSeek-R1 — and on to agent harnesses, memory systems, and vision-language models. If a concept matters, we don't just explain it. We build it, break it, and rebuild it until the intuition is earned.

> *"What I cannot create, I do not understand."* — Richard Feynman

---

## Table of Contents

### 01 - Machine Learning

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Data Processing](01%20-%20Machine%20Learning/01%20-%20Data%20Processing.ipynb) | Bias-variance tradeoff, feature scaling, data splitting, and preprocessing pipelines |
| 02 | [Regression](01%20-%20Machine%20Learning/02%20-%20Regression.ipynb) | Linear and polynomial regression — cost functions, gradient descent, and regularization |
| 03 | [Classification](01%20-%20Machine%20Learning/03%20-%20Classification.ipynb) | Logistic regression, SVMs, decision trees, random forests, and ensemble methods |
| 04 | [Clustering](01%20-%20Machine%20Learning/04%20-%20Clustering.ipynb) | K-Means, DBSCAN, hierarchical clustering — algorithms, objective functions, and evaluation |
| 05 | [Dimension Reduction](01%20-%20Machine%20Learning/05%20-%20Dimension%20Reduction.ipynb) | PCA derivation, eigenvalue decomposition, and t-SNE for high-dimensional data |

### 02 - Deep Learning Foundation

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Neural Network Foundations](02%20-%20Deep%20Learning%20Foundation/01%20-%20Neural%20Network%20Foundations.ipynb) | NumPy vectorization, broadcasting, forward/backward pass from scratch |
| 02 | [Activation Functions](02%20-%20Deep%20Learning%20Foundation/02%20-%20Activation%20Functions.ipynb) | Sigmoid, tanh, ReLU, GELU — why activations matter, saturation, and dying neurons |
| 03 | [Weight Initialization](02%20-%20Deep%20Learning%20Foundation/03%20-%20Weight%20Initialization.ipynb) | Why zero init fails, variance explosion/vanishing, Xavier and He initialization proofs |
| 04 | [Normalization](02%20-%20Deep%20Learning%20Foundation/04%20-%20Normalization.ipynb) | Batch norm, layer norm, group norm — internal covariate shift and loss landscape smoothing |
| 05 | [Regularization](02%20-%20Deep%20Learning%20Foundation/05%20-%20Regularization.ipynb) | L2 weight decay, dropout, early stopping — fighting overfitting with math |
| 06 | [Residual Connection](02%20-%20Deep%20Learning%20Foundation/06%20-%20Residual%20Connection.ipynb) | The degradation problem, skip connections, and why deeper networks can fail without them |
| 07 | [Loss Function](02%20-%20Deep%20Learning%20Foundation/07%20-%20Loss%20Function.ipynb) | BCE, cross-entropy derivations — why sigmoid+BCE and softmax+CE produce clean gradients |
| 08 | [Optimizer](02%20-%20Deep%20Learning%20Foundation/08%20-%20Optimizer.ipynb) | SGD, momentum, RMSProp, Adam — from vanilla gradient descent to adaptive learning rates |
| 09 | [Model Classification](02%20-%20Deep%20Learning%20Foundation/09%20-%20Model%20Classification.ipynb) | End-to-end image classification on CIFAR-10 applying all the foundations above |

### 03 - Large Language Model

#### RNN

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Vanilla RNN](03%20-%20Large%20Language%20Model/01%20-%20RNN/01%20-%20Vanilla%20RNN.ipynb) | RNN, GRU and LSTM cells from scratch — hidden states, BPTT, vanishing/exploding gradients, character-level LM |
| 02 | [RNN with Attention](03%20-%20Large%20Language%20Model/01%20-%20RNN/02%20-%20RNN%20with%20Attention.ipynb) | Seq2seq bottleneck problem, Bahdanau vs Luong attention for date format translation |

#### Training Strategy

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Data Processing](03%20-%20Large%20Language%20Model/02%20-%20Training%20Strategy/01%20-%20Data%20Processing.ipynb) | Pretraining data pipelines — heuristic filters, deduplication, CCNet perplexity and classifier quality filtering, data mixing and annealing |
| 02 | [Distributed Training](03%20-%20Large%20Language%20Model/02%20-%20Training%20Strategy/02%20-%20Distributed%20Training.ipynb) | GPU programming to multi-GPU training — SIMT, memory hierarchy, roofline model, Triton kernels, profiling, DDP, tensor and pipeline parallelism |

#### Transformer Models

| # | Notebook | Description |
|---|----------|-------------|
| A01 | [Attention Mechanism](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/A01%20-%20Attention%20Mechanism.ipynb) | Self-attention and scaled dot-product, multi-head attention, Flash and sliding-window/sparse attention |
| A02 | [Transformer](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/A02%20-%20Transformer.ipynb) | Full transformer architecture from scratch — masking, positional encoding, multi-head attention, encoder-decoder |
| B01 | [BERT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/B01%20-%20BERT.ipynb) | Bidirectional encoder — WordPiece tokenization, MLM, NSP, and the fine-tuning paradigm |
| B02 | [ColBERT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/B02%20-%20ColBERT.ipynb) | Late interaction retrieval — MaxSim scoring, query augmentation, token-level matching |
| C01 | [nanoGPT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C01%20-%20nanoGPT.ipynb) | GPT-2 from scratch — byte-level BPE tokenization, causal self-attention, autoregressive decoding |
| C02 | [LLaMA](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C02%20-%20LLaMA.ipynb) | LLaMA architecture deep dive — RMSNorm, RoPE, SwiGLU, grouped-query attention |
| C03 | [DeepSeek](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C03%20-%20DeepSeek.ipynb) | Multi-head Latent Attention (MLA), fine-grained MoE with shared experts, multi-token prediction, mHC, compressed sparse attention |
| C04 | [Qwen](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C04%20-%20Qwen.ipynb) | Advanced RoPE scaling — Position Interpolation, NTK-Aware, Dynamic NTK, YaRN |

#### Text Retrieval & NLP

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Text Embedding](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/01%20-%20Text%20Embedding.ipynb) | Cosine similarity, dot product, L2 distance — similarity metrics and embedding spaces |
| 02 | [HNSW](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/02%20-%20HNSW.ipynb) | Approximate nearest neighbors — HNSW, Product Quantization, IVF for vector search |
| 03 | [Topic Modeling](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/03%20-%20Topic%20Modeling.ipynb) | Discovering latent topics from text corpora |
| 04 | [NER](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/04%20-%20NER.ipynb) | Named Entity Recognition — BIO tagging, CoNLL-2003, BERT token classification, GLiNER zero-shot spans |
| 05 | [RAG](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/05%20-%20RAG.ipynb) | Retrieval-Augmented Generation — chunking, hybrid search, HyDE, RRF, Self-RAG/CRAG/agentic RAG, reranking, evaluation |
| 06 | [Graph RAG](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/06%20-%20Graph%20RAG.ipynb) | Knowledge-graph retrieval — LLM entity/relation extraction, entity linking, multi-hop graph traversal |

#### Post-Training Alignment

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [SFT](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/01%20-%20SFT.ipynb) | Supervised Fine-Tuning — chat templates, conversational vs completion formats, assistant-only loss masking, packing |
| 02 | [Reward Model](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/02%20-%20Reward%20Model.ipynb) | ORM vs PRM — Bradley-Terry loss, step-level credit assignment for reasoning |
| 03 | [DPO vs ORPO and SimPO](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/03%20-%20DPO%20vs%20ORPO%20and%20SimPO.ipynb) | Direct Preference Optimization — aligning LLMs with human preferences without RL |
| 04 | [GRPO with RLVR](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/04%20-%20GRPO%20with%20RLVR.ipynb) | Group Relative Policy Optimization — the algorithm behind DeepSeek-R1, with verifiable rewards |
| 05 | [PEFT (LoRA / QLoRA)](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/05%20-%20Parameter-Efficient%20Fine-Tuning%20(PEFT).ipynb) | LoRA and QLoRA from scratch — low-rank adaptation, 4-bit quantization, 99.6% fewer parameters |
| 06 | [Abliteration](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/06%20-%20Abliteration.ipynb) | Mechanistic interpretability — finding and removing the refusal direction in activation space |

#### Model Compression

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Distillation](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/01%20-%20Distillation.ipynb) | Knowledge distillation — response-level SFT, logit-level KD, rejection sampling |
| 02 | [Model Pruning](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/02%20-%20Model%20Pruning.ipynb) | Unstructured and structured pruning — layer-wise vs global, importance criteria, the coupling problem, iterative vs one-shot |
| 03 | [Quantization](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/03%20-%20Quantization.ipynb) | FP32 to INT4 — numeric formats, quantization schemes, memory-accuracy tradeoffs |

#### Agentic LLM

| # | Notebook | Description |
|---|----------|-------------|
| A01 | [LLM Prompting](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A01%20-%20LLM%20Prompting.ipynb) | Prompt design patterns, few-shot, CoT/self-consistency, structured output, prompt injection defenses |
| A02 | [Agent Harness](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A02%20-%20Agent%20Harness.ipynb) | The agent loop from scratch — tool system, planning, subagents, skills, context compaction, task system, agent teams |
| A03 | [Agent Operation](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A03%20-%20Agent%20Operation.ipynb) | Running agents in production — observability, token budgeting, prompt caching, model routing, agent testing |
| A04 | [Self Evolution Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A04%20-%20Self%20Evolution%20Agent.ipynb) | Agents that improve themselves — Reflexion, GEPA evolutionary prompt optimization, skill evolution with constraint gates, ADAS |
| A05 | [AI Agent Memory](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A05%20-%20AI%20Agent%20Memory.ipynb) | Memory architectures — Mem0 KV store, MemGPT/Letta tiers, Zep temporal knowledge graphs, hybrid retrieval, consolidation, procedural memory |
| B01 | [LangGraph Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B01%20-%20LangGraph%20Agent.ipynb) | Cyclic state graphs with LangGraph — ReAct, plan-and-execute, memory, multi-agent supervisors, MCP, LangSmith tracing |
| B02 | [Code Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B02%20-%20Code%20Agent.ipynb) | Multi-agent repository auditing — code knowledge graphs, structural detectors, inter-procedural data flow, LLM validators |

#### Production & Inference

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Generation](03%20-%20Large%20Language%20Model/08%20-%20Production%20%26%20Inference/01%20-%20Generation.ipynb) | Text generation from scratch — KV-cache, greedy/beam/sampling, batched and continuous batching, speculative and constrained decoding |

#### LLM Evaluation

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [LLM Evaluation](03%20-%20Large%20Language%20Model/09%20-%20LLM%20Evaluation/01%20-%20LLM%20Evaluation.ipynb) | Perplexity, BLEU/ROUGE, BERTScore, calibration (ECE), LLM-as-a-judge with bias mitigation, and Elo ratings with bootstrap CIs |

### 04 - Computer Vision

#### Image Processing

| # | Notebook | Description |
|---|----------|-------------|
| 1 | [Image Processing](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/1%20-%20Image_Processing.ipynb) | OpenCV basics — I/O, drawing, blending, thresholding, blurring, morphology, color filtering |
| 2 | [Image Detection](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/2%20-%20Image%20Detection.ipynb) | Template matching, corners, Canny edges, contours, ORB feature matching, face and QR detection |
| 3 | [Image Analysis](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/3%20-%20Image%20Analysis.ipynb) | Histograms and equalization, dominant colors via K-Means, structural similarity |
| 4 | [Motion Tracking](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/4%20-%20Motion%20Tracking.ipynb) | Lucas-Kanade and dense optical flow, Mean Shift and CamShift tracking |

#### Deep Learning for Vision

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [CNN Foundations](04%20-%20Computer%20Vision/01%20-%20CNN%20Foundations.ipynb) | Convolutions from scratch in NumPy — zero-padding, forward/backward pass, pooling, and gradient derivations |
| 02 | [Transfer Learning](04%20-%20Computer%20Vision/02%20-%20Transfer%20Learning.ipynb) | Feature extraction vs fine-tuning on CIFAR-10 — ImageNet normalization, layer freezing strategies |
| 03 | [Object Detection](04%20-%20Computer%20Vision/03%20-%20Object%20Detection.ipynb) | IoU, NMS, anchor box assignment, and YOLO output decoding — built from scratch |
| 04 | [Image Segmentation](04%20-%20Computer%20Vision/04%20-%20Image%20Segmentation.ipynb) | U-Net encoder/decoder from scratch — skip connections, pixel-wise loss, SegFormer inference |
| 05 | [Metric Learning](04%20-%20Computer%20Vision/05%20-%20Metric%20Learning.ipynb) | Siamese networks, contrastive loss, triplet loss, and FaceNet — embedding spaces for unseen classes |
| 06 | [Vision Transformers](04%20-%20Computer%20Vision/06%20-%20Vision%20Transformers.ipynb) | ViT, DeiT, and Swin from scratch — patch embedding, multi-head self-attention, hierarchical windows |
| 07 | [Contrastive Learning](04%20-%20Computer%20Vision/07%20-%20Contrastive%20Learning.ipynb) | SimCLR, DINOv2, and CLIP vs SigLIP — self-supervised and image-text contrastive pretraining |
| 08 | [Diffusion Model](04%20-%20Computer%20Vision/08%20-%20Diffusion%20Model.ipynb) | DDPM, DDIM, Stable Diffusion — forward/reverse process, noise schedules, ContextUNet |
| 09 | [Model Explainability](04%20-%20Computer%20Vision/09%20-%20Model%20Explainability.ipynb) | Saliency maps, GradCAM, Integrated Gradients, and SHAP on ResNet-50 |

### 05 - Multi-Modal

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Bridge Architecture](05%20-%20Multi-Modal/01%20-%20Bridge%20Architecture.ipynb) | Connecting frozen ViT to frozen LLM — LLaVA projectors, Flamingo Perceiver, BLIP-2 Q-Former, MoE bridges |
| 02 | [Vision Language Model](05%20-%20Multi-Modal/02%20-%20Vision%20Language%20Model.ipynb) | Qwen-VL style VLM from scratch — TinyViT, MLP projector, mRoPE, visual token insertion, Stage 1 training |
| 03 | [Instruction Tuning](05%20-%20Multi-Modal/03%20-%20Instruction%20Tuning.ipynb) | Stage 2 on a pretrained VLM — SmolVLM + ChartQA LoRA SFT, multimodal loss masking, resolution vs. visual token budget, grounding diagnostics |
| 04 | [Reasoning & Inference](05%20-%20Multi-Modal/04%20-%20Reasoning%20%26%20Inference.ipynb) | VLM inference pipeline — decoding strategies, streaming, chain-of-thought, visual grounding, evaluation |
| 05 | [Audio & Speech](05%20-%20Multi-Modal/05%20-%20Audio%20%26%20Speech.ipynb) | Waveforms to Mel spectrograms from scratch — audio encoders, Whisper, Phi-4 multimodal speech |
| 06 | [Video](05%20-%20Multi-Modal/06%20-%20Video.ipynb) | Video understanding — spatial-temporal attention, ViViT, dynamic FPS sampling, text-timestamp alignment |
| 07 | [Visual Agent & Computer Use](05%20-%20Multi-Modal/07%20-%20Visual%20Agent%20and%20Computer%20Use.ipynb) | VLMs that act on GUIs — perception, planning, action loops, computer-use agents |
| 08 | [Native Multimodal](05%20-%20Multi-Modal/08%20-%20Native%20Multimodal.ipynb) | Any-to-any unified token spaces — Chameleon, Transfusion, Emu3, Janus Pro with VQ-VAE tokenizers |

### Coming Soon

| Topic | Description |
|-------|-------------|
| Model Serving | vLLM, PagedAttention, prefill vs decode, autoscaling, and production deployment |
| AI Governance & Security | Red teaming, toxicity benchmarks, bias evaluation, hallucination detection, adversarial robustness |

---

More work is coming. This repository is actively maintained and expanding as the field evolves.
