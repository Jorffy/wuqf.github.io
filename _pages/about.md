---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 👋 About Me 
My research interests lie in the field of Natural Language Processing and Large Language Models, specifically on Multimodal Analysis, Sentiment Detection and Multimodal Large Language Models. <a href='https://scholar.google.com/citations?user=zo8SfrMAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
<!-- I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=zo8SfrMAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=zo8SfrMAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->


<!-- # 🔥 News
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurocomputing 2025</div><img src='images/DAIE_model.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Dual-Level Adaptive Incongruity-Enhanced Model for Multimodal Sarcasm Detection**](https://doi.org/10.1016/j.neucom.2024.128689)

*Neurocomputing 2025*

**Qiaofeng Wu**, Wenlong Fang, Weiyu Zhong, Fenghuan Li, Yun Xue and Bo Chen

<a href="https://doi.org/10.1016/j.neucom.2024.128689" target="_blank">
    <img alt="Paper DAIE" src="https://img.shields.io/badge/%F0%9F%93%96%20Paper-DAIE-C6E7FF?logoColor=white" />
</a>
<a href="https://github.com/Jorffy/DAIE" target="_blank">
    <img alt="Github DAIE" src="https://img.shields.io/badge/Github-DAIE-F2F2F2?logo=github" />
</a>
[![](https://img.shields.io/github/stars/Jorffy/DAIE)](https://github.com/Jorffy/DAIE)

<!-- - A **D**ual-Level **A**daptive **I**ncongruity-**E**nhanced Model (**DAIE**) is proposed for Multimodal Sarcasm Detection. 
- By leveraging Patch-based Reconstructed Image (PRI), the Token-Level Contrastive Learning (TLCL) effectively diminishes the presence of common features among visually similar images. 
- The Graph-Level Contrastive Learning (GLCL) module with Negative pair Similarity Weights (NSW) dynamically adjusts the inter-node weights across the Graph Attention Networks (GAT), guided by negative similarity weights. 
- Experimental results on a publicly available multimodal sarcasm detection dataset demonstrate the superiority of our proposed method. -->

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/NoteMR.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Notes-guided MLLM Reasoning: Enhancing MLLM with Knowledge and Visual Notes for Visual Question Answering**](https://openaccess.thecvf.com/content/CVPR2025/html/Fang_Notes-guided_MLLM_Reasoning_Enhancing_MLLM_with_Knowledge_and_Visual_Notes_CVPR_2025_paper.html)

*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025*

Wenlong Fang, **Qiaofeng Wu**, Jing Chen and Yun Xue

<a href="https://openaccess.thecvf.com/content/CVPR2025/html/Fang_Notes-guided_MLLM_Reasoning_Enhancing_MLLM_with_Knowledge_and_Visual_Notes_CVPR_2025_paper.html" target="_blank">
    <img alt="Paper NoteMR" src="https://img.shields.io/badge/%F0%9F%93%96%20Paper-NoteMR-C6E7FF?logoColor=white" />
</a>
<a href="https://github.com/Jorffy/NoteMR" target="_blank">
    <img alt="Github NoteMR" src="https://img.shields.io/badge/Github-NoteMR-F2F2F2?logo=github" />
</a>
[![](https://img.shields.io/github/stars/Jorffy/NoteMR)](https://github.com/Jorffy/NoteMR)

<!-- - **Note**s-guided **M**LLM **R**easoning (**NoteMR**) is proposed for Knowledge-Based Visual Question Answering (KB-VQA) tasks.
- Explicit external knowledge and images are integrated to generate knowledge notes, which filter irrelevant explicit knowledge and identify MLLM’s internal relevant implicit knowledge.
- Highly correlated regions between images and knowledge notes are extracted as image notes, enhancing the model’s fine-grained visual perception and mitigating MLLM-induced hallucinations.
- The combination of knowledge notes and image notes enables MLLM to comprehensively understand image-question pairs and improve reasoning capabilities.
- State-of-the-art performance is achieved on OK-VQA and A-OKVQA datasets, verifying the framework’s robustness and effectiveness across diverse scenarios. -->

</div>
</div>

- [Ambiguity-aware Multi-level Incongruity Fusion Network for Multi-Modal Sarcasm Detection](https://aclanthology.org/2025.coling-main.26/), Kuntao Li, Yifan Chen, **Qiaofeng Wu**, Weixing Mai, Fenghuan Li and Yun Xue, *COLING 2025*
- [D2R: Dual-Branch Dynamic Routing Network for Multimodal Sentiment Detection](https://aclanthology.org/2024.emnlp-main.207), Yifan Chen, Kuntao Li, Weixing Mai, **Qiaofeng Wu**, Yun Xue and Fenghuan Li, *EMNLP 2024*
- [A Semantic Enhancement Framework for Multimodal Sarcasm Detection](https://doi.org/10.3390/math12020317), Weiyu Zhong, Zhengxuan Zhang , **Qiaofeng Wu**, Yun Xue and Qianhua Cai, *Mathematic 2024*
- [Keyword-Enhanced Multi-Expert Framework for Hate Speech Detection](https://doi.org/10.3390/math10244706), Weiyu Zhong, **Qiaofeng Wu**, Guojun Lu, Yun Xue and Xiaohui Hu, *Mathematic 2022*

# 📖 Educations
- *2022.06 - 2025.06*, South China Normal University. 
- *2018.09 - 2022.06*, South China Normal University. 

# 💻 Internships
- *2024.06 - 2024.09*, [IFLYTEK](https://www.iflytek.com/cn/), China.
- *2024.12 - 2025.06*, [KINGSOFT](https://www.kingsoft.com/), China.