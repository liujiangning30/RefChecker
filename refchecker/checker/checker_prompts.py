JOINT_CHECKING_PROMPT_Q = """I have a list of claims that made by a language model to a question, please help me for checking whether the claims can be entailed according to the provided reference which is related to the question. 
The reference is a list of passages, and each of the claims is represented as a triplet formatted with ("subject", "predicate", "object").

If the claim is supported by ANY passage in the reference, answer 'Entailment'. 
If NO passage in the reference entail the claim, and the claim is contradicted with some passage in the reference, answer 'Contradiction'.
If NO passage entail or contradict with claim, or DOES NOT contain information to verify the claim, answer 'Neutral'. 

Please DO NOT use your own knowledge for the judgement, just compare the reference and the claim to get the answer.

### Question:
[QUESTION]

### Reference:
[REFERENCE]

### Claims:
[CLAIMS]


Your answer should always be only a list of labels, each of the labels is a single word in ['Entailment', 'Neutral', 'Contradiction'], for example, you should output a list like follows:

Entailment
Neutral
Contradiction
Neutral


DO NOT add explanations or you own reasoning to the output, only output the label list.
"""

JOINT_CHECKING_PROMPT_Q_CN = \
"""
我有一个语言模型对某个问题做出的主张列表，请帮助我检查这些主张是否可以根据与该问题相关的参考资料得出结论。参考资料是一系列段落，每个主张以 ("主语", "谓语", "宾语") 的三元组格式表示。

如果参考资料中的任意段落支持该主张，请回答“Entailment”（蕴涵）。
如果参考资料中没有任何段落支持该主张，并且参考资料中的某些段落与该主张相矛盾，请回答“Contradiction”（矛盾）。
如果参考资料中没有任何段落支持或反驳该主张，或者不包含验证该主张的信息，请回答“Neutral”（中立）。

请不要使用你自己的知识进行判断，仅根据参考资料与主张进行比较以得出答案。

### 问题：
[QUESTION]

### 参考资料：
[REFERENCE]

### 主张：
[CLAIMS]

你的答案应始终只是一系列标签，每个标签都是 ['Entailment', 'Neutral', 'Contradiction'] 中的一个词。例如，你应该输出如下列表：

Entailment  
Neutral  
Contradiction  
Neutral

不要添加解释或你自己的推理，答案中只输出标签列表。
"""

JOINT_CHECKING_PROMPT= """I have a list of claims that made by a language model, please help me for checking whether the claims can be entailed according to the provided reference. 
The reference is a list of passages, and each of the claims is represented as a triplet formatted with ("subject", "predicate", "object").

If the claim is supported by ANY passage in the reference, answer 'Entailment'. 
If NO passage in the reference entail the claim, and the claim is contradicted with some passage in the reference, answer 'Contradiction'.
If NO passage entail or contradict with claim, or DOES NOT contain information to verify the claim, answer 'Neutral'. 

Please DO NOT use your own knowledge for the judgement, just compare the reference and the claim to get the answer.

### Reference:
[REFERENCE]

### Claims:
[CLAIMS]


Your answer should always be only a list of labels, each of the labels is a single word in ['Entailment', 'Neutral', 'Contradiction'], for example, you should output a list like follows:

Entailment
Neutral
Contradiction
Neutral


DO NOT add explanations or you own reasoning to the output, only output the label list.
"""


LLM_CHECKING_PROMPT_Q = \
"""I have a claim that made by a language model to a question, please help me for checking whether the claim can be entailed according to the provided reference which is related to the question. 
The reference is a list of passages, and the claim is represented as a triplet formatted with ("subject", "predicate", "object").

If the claim is supported by ANY passage in the reference, answer 'Entailment'. 
If NO passage in the reference entail the claim, and the claim is contradicted with some passage in the reference, answer 'Contradiction'.
If NO passage entail or contradict with claim, or DOES NOT contain information to verify the claim, answer 'Neutral'. 

Please DO NOT use your own knowledge for the judgement, just compare the reference and the claim to get the answer.

### Question:
{question}

### Reference:
{reference}

### Claim:
{claim}

Your answer should always be only a single word in ['Entailment', 'Neutral', 'Contradiction']. DO NOT add explanations or you own reasoning to the output.
"""

LLM_CHECKING_PROMPT = \
"""I have a claim that made by a language model, please help me for checking whether the claim can be entailed according to the provided reference. 
The reference is a list of passages, and the claim is represented as a triplet formatted with ("subject", "predicate", "object").

If the claim is supported by ANY passage in the reference, answer 'Entailment'. 
If NO passage in the reference entail the claim, and the claim is contradicted with some passage in the reference, answer 'Contradiction'.
If NO passage entail or contradict with claim, or DOES NOT contain information to verify the claim, answer 'Neutral'. 

Please DO NOT use your own knowledge for the judgement, just compare the reference and the claim to get the answer.

### Reference:
{reference}

### Claim:
{claim}

Your answer should always be only a single word in ['Entailment', 'Neutral', 'Contradiction']. DO NOT add explanations or you own reasoning to the output.
"""


SUBSENTENCE_CLAIM_CHECKING_PROMPT = \
"""I have a claim that made by a language model, please help me for checking whether the claim can be entailed according to the provided reference. 
The reference is a list of passages, and the claim is a sentence.

If the claim is supported by ANY passage in the reference, answer 'Entailment'. 
If NO passage in the reference entail the claim, and the claim is contradicted with some passage in the reference, answer 'Contradiction'.
If NO passage entail or contradict with claim, or DOES NOT contain information to verify the claim, answer 'Neutral'. 

Please DO NOT use your own knowledge for the judgement, just compare the reference and the claim to get the answer.

### Reference:
{reference}

### Claim:
{claim}

Your answer should always be only a single word in ['Entailment', 'Neutral', 'Contradiction']. DO NOT add explanations or you own reasoning to the output.
"""