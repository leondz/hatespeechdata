
This page catalogues datasets annotated for hate speech, online abuse, and offensive language. They may be useful for e.g. training a natural language processing system to detect this language.

The list is maintained by [Leon Derczynski](https://www.derczynski.com/) and [Bertie Vidgen](https://www.turing.ac.uk/people/researchers/bertie-vidgen).

Please make contributions via pull request or email. Accompanying [data statements](https://www.mitpressjournals.org/doi/abs/10.1162/tacl_a_00041) preferred for all corpora.

If you use these resources, please cite (and read!) our paper: [Directions in Abusive Language Training Data: Garabge In, Garbage Out](https://arxiv.org/abs/2004.01670).


## List of datasets

### Arabic
__1. Are They our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere__

* Reference: Albadi, N., Kurdi, M. and Mishra, S., 2018. Are they Our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere. In: International Conference on Advances in Social Networks Analysis and Mining. Barcelona, Spain: IEEE, pp.69-76. 
 * Link to publication: [https://ieeexplore.ieee.org/document/8508247](https://ieeexplore.ieee.org/document/8508247)
 * Link to data: https://github.com/nuhaalbadi/Arabic_hatespeech 
 * Task description: Binary (Hate, Not) 
 * Details of task: Religious subcategories 
 * Size of dataset: 6136 
 * Percentage abusive: 0.45 
 * Language: Arabic 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: CrowdFlower: 234 annotators. Annotatrs with accuracy below were 70% excluded (based on 100 gold standard test questions). On average, there were 3 annotations per tweet
 * Annotation agreement: 81% for hate/not and 55% for the religious group which was targetted
 
 
 2. __Multilingual and Multi-Aspect Hate Speech Analysis (Arabic)__

* Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 
* Link to publication: [https://arxiv.org/abs/1908.11049](https://arxiv.org/abs/1908.11049)
* Link to data: https://github.com/HKUST-KnowComp/MLMA_hate_speech 
* Task description: Detailed taxonomy with cross-cutting attributes:
HOSTILITY (Abusive, Hateful, Offensive, Disrespectful, Fearful, Normal)
DIRECTNESS (Direct/indirect)
Target attribute (Origin [covers race, ethnicity and nationality], Gender, Sexual Orientation, Religion, Disability, Other)
Target Group (16 identified, of which the five most common are: Individual, Other, Women, Special needs, African Descent)
Annotator sentiment [i.e. how the annotators felt on seeing the tweet] (Disgust, Shock, Anger, Sadness, Fear, Confusion, Indifference) 
* Details of task: Gender, Sexual orientation, Religion, Disability 
* Size of dataset: 3353 
* Percentage abusive: 0.64 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Annotation process: Annotators on Mechanical Turk.
5 annotators per entry, with majority voting to decide final labels.
For the more subjetive labels, all of the annotations were retained(i.e. hostility type and the annotator’s sentiment labels).
Annotators were provided with definitions of offensive words from Urban Dictionary.
Annotators were reminded 'not to let their personal opinions about the topics being discussed in the tweets influence their annotation decisions'.
* Annotation agreement: Krippendorf score: 0.202 
 
 
 3. __L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language__
 * Reference: Mulki, H., Haddad, H., Bechikh, C. and Alshabani, H., 2019. L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.111-118. 
 * Link to publication: [https://www.aclweb.org/anthology/W19-3512](https://www.aclweb.org/anthology/W19-3512)
 * Link to data: https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset 
 * Task description: Ternary (Hate, Abusive, Normal) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 5846 
 * Percentage abusive: 0.38 
 * Language: Arabic 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Three annotators coded up each tweet. 
 * Annotation agreement: Pairwise percentage agreement: 78.43%, 87.24%, 78.77%
Cohen's K: 0.599, 0.758, 0.594
Krippendorf's Alpha: 76.5%
3/3 agreement (4,222), 2/3 agreement (1,624), conflict (154) 
  
 4. __Abusive Language Detection on Arabic Social Media (Twitter)__
 * Reference: Mubarak, H., Darwish, K. and Magdy, W., 2017. Abusive Language Detection on Arabic Social Media. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.52-56. 
 * Link to publication: [https://www.aclweb.org/anthology/W17-3008](https://www.aclweb.org/anthology/W17-3008)* Link to data: http://alt.qcri.org/~hmubarak/offensive/ObsceneWords.txt

http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx 
 * Task description: Ternary (Obscene, Offensive but not obscene, Clean) 
 * Details of task: Incivility 
 * Size of dataset: 1100 
 * Percentage abusive: 0.59 
 * Language: Arabic 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 3 crowdflower workers annotate each tweet. They are given the context (thread of replies) for each tweet. 
 * Annotation agreement: 85% 
  
 5. __Abusive Language Detection on Arabic Social Media (Al Jazeera)__
 * Reference: Mubarak, H., Darwish, K. and Magdy, W., 2017. Abusive Language Detection on Arabic Social Media. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.52-56. 
 * Link to publication: [https://www.aclweb.org/anthology/W17-3008](https://www.aclweb.org/anthology/W17-3008)* Link to data: http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx 
 * Task description: Ternary (Obscene, Offensive but not obscene, Clean) 
 * Details of task: Incivility 
 * Size of dataset: 32000 
 * Percentage abusive: 0.81 
 * Language: Arabic 
 * Level of annotation: Posts 
 * Platform: AlJazeera 
 * Medium: Text 
 * Annotation process: 3 crowdflower workers annotate each tweet. 
 * Annotation agreement: 87% 
  
 6. __Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic__
 * Reference: Alakrot, A., Murray, L. and Nikolov, N., 2018. Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic. Procedia Computer Science, 142, pp.174-181. 
 * Link to publication: [https://www.sciencedirect.com/science/article/pii/S1877050918321756] (https://www.sciencedirect.com/science/article/pii/S1877050918321756)* Link to data: https://onedrive.live.com/?authkey=!ACDXj_ZNcZPqzy0&id=6EF6951FBF8217F9!105&cid=6EF6951FBF8217F9 
 * Task description: Binary (Offensive, Not) 
 * Details of task: Incivility 
 * Size of dataset: 15050 
 * Percentage abusive: 0.39 
 * Language: Arabic 
 * Level of annotation: Posts 
 * Platform: YouTube 
 * Medium: Text 
 * Annotation process: 3 annotators code each bit of content.
Final decision is made on 2/3 majority decision
Content which at least one person did not label (as they were 'unsure') were excluded (848 bits)
 
 * Annotation agreement: 71%
Pairwise Kappa: 0.698, 0.579, 0.512 
 
### Croatian
 7. __Datasets of Slovene and Croatian Moderated News Comments__
 * Reference: Ljubešić, N., Erjavec, T. and Fišer, D., 2018. Datasets of Slovene and Croatian Moderated News Comments. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.124-131. 
 * Link to publication: [https://www.aclweb.org/anthology/W18-5116] (https://www.aclweb.org/anthology/W18-5116)* Link to data: http://hdl.handle.net/11356/1202 
 * Task description: Binary (Deleted, Not) 
 * Details of task: Flagged content 
 * Size of dataset: 17000000 
 * Percentage abusive: 0.02 
 * Language: Croatian 
 * Level of annotation: Posts 
 * Platform: 24sata website 
 * Medium: Text 
 * Annotation process: Flagged by professional moderators 
 * Annotation agreement: N/A 

### Danish
 8. __Offensive Language and Hate Speech Detection for Danish__
 * Reference: Sigurbergsson, G. and Derczynski, L., 2019. Offensive Language and Hate Speech Detection for Danish. ArXiv. 
 * Link to publication: [http://www.derczynski.com/papers/danish_hsd.pdf] (http://www.derczynski.com/papers/danish_hsd.pdf)* Link to data: https://sites.google.com/site/offensevalsharedtask/home 
 * Task description: Branching structure of tasks:
Binary (Offensive, Not)
Within Offensive (Target, Not)
Within Target (Individual, Group, Other) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 3600 
 * Percentage abusive: 0.12 
 * Language: Danish 
 * Level of annotation: Posts 
 * Platform: Twitter, Reddit, newspaper comments 
 * Medium: Text 
 * Annotation process: trained annotators, agreement measured on test partition 
 * Annotation agreement: not given 


### English
 9. __Automated Hate Speech Detection and the Problem of Offensive Language__
 * Reference: Davidson, T., Warmsley, D., Macy, M. and Weber, I., 2017. Automated Hate Speech Detection and the Problem of Offensive Language. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1703.04009.pdf] (https://arxiv.org/pdf/1703.04009.pdf)* Link to data: https://github.com/t-davidson/hate-speech-and-offensive-language 
 * Task description: Hierarchy (Hate, Offensive, Neither) 
 * Details of task: Hate per se 
 * Size of dataset: 24802 
 * Percentage abusive: 0.06 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Crowdflower: definitions + paragraph of description given (instructions not made public). 3 + people annotated each tweet. Majority decision taken 
 * Annotation agreement: 92% agreement; Only tweets with a majority decision were retained (out of 24,802 out of 25,000 tweets in the final dataset) 
  
 10. __Hate Speech Dataset from a White Supremacy Forum__
 * Reference: de Gibert, O., Perez, N., Garcia-Pablos, A. and Cuadros, M., 2018. Hate Speech Dataset from a White Supremacy Forum. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1809.04444.pdf] (https://arxiv.org/pdf/1809.04444.pdf)* Link to data: https://github.com/aitor-garcia-p/hate-speech-dataset 
 * Task description: Ternary (Hate, Relation, Not) - Hate is defined at a general level to include all targeted groups/identities 
 * Details of task: Hate per se 
 * Size of dataset: 9916 
 * Percentage abusive: 0.11 
 * Language: English 
 * Level of annotation: Posts - with context of the converstaional thread taken into account 
 * Platform: Stormfront 
 * Medium: Text 
 * Annotation process: 1,144 sentences were annotated by 3 experts. Guidelines were then updated. Then, 1,018 sentences were annotated by three experts. The remaining sentences were annotated by just one person. 
 * Annotation agreement: 1st round of annotation: 91%, 0.614 average Cohen's pairwise Kappa, 0.607 Fleiss' Kappa
2nd round of annotation: 91%, 0.627 average Cohen's pairwise Kappa, 0.632 Fleiss' Kappa
 
  
 11. __Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter__
 * Reference: Waseem, Z. and Horvy, D., 2016. Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter. In: Proceedings of the NAACL Student Research Workshop. San Diego, California: Association for Computational Linguistics, pp.88-93. 
 * Link to publication: [https://www.aclweb.org/anthology/N16-2013] (https://www.aclweb.org/anthology/N16-2013)* Link to data: https://github.com/ZeerakW/hatespeech 
 * Task description: 3-topic (Sexist, Racist, Not) 
 * Details of task: Racism, Sexism 
 * Size of dataset: 16914 
 * Percentage abusive: 0.32 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 2 authors manually annotate + outside expert abjudicates in cases of disagreement (25-year old woman studyiing gender studies and a non-activist feminist) 
 * Annotation agreement: 0.84 Cohen's K. 98% of all disagreements set to 'not' 
  
 12. __Detecting Online Hate Speech Using Context Aware Models__
 * Reference: Gao, L. and Huang, R., 2018. Detecting Online Hate Speech Using Context Aware Models. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1710.07395.pdf] (https://arxiv.org/pdf/1710.07395.pdf)* Link to data: https://github.com/sjtuprog/fox-news-comments 
 * Task description: Binary (Hate / not). For all targets 
 * Details of task: Hate per se 
 * Size of dataset: 1528 
 * Percentage abusive: 0.28 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Fox News 
 * Medium: Text 
 * Annotation process: 2 experts for first 648 comments: they used the Nobata guidelines for annotation. They adopted a slightly weird 2-stage annotation, using one person for the last 880 comments 
 * Annotation agreement: 0.98 Cohen's Kappa (on 648 comments, taken from 4 threads) 
  
 13. __Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter__
 * Reference: Waseem, Z., 2016. Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter. In: Proceedings of 2016 EMNLP Workshop on Natural Language Processing and Computational Social Science. Copenhagen, Denmark: Association for Computational Linguistics, pp.138-142. 
 * Link to publication: [https://pdfs.semanticscholar.org/3eeb/b7907a9b94f8d65f969f63b76ff5f643f6d3.pdf] (https://pdfs.semanticscholar.org/3eeb/b7907a9b94f8d65f969f63b76ff5f643f6d3.pdf)* Link to data: https://github.com/ZeerakW/hatespeech 
 * Task description: Multi-topic (sexist, racist, not, both) 
 * Details of task: Racism, Sexism 
 * Size of dataset: 4033 
 * Percentage abusive: 0.16 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: First, Experts (including feminist and anti-racist activists) annotate the tweets. Then, CF amateur annotators re-annotate them. No IRR tests for the Experts as they are treated 'as a single entity'. (139). 
 * Annotation agreement: 0.57 Kappa for CF amateur annotations 
  
 14. __When Does a Compliment Become Sexist? Analysis and Classification of Ambivalent Sexism Using Twitter Data__
 * Reference: Jha, A. and Mamidi, R., 2017. When does a Compliment become Sexist? Analysis and Classification of Ambivalent Sexism using Twitter Data. In: Proceedings of the Second Workshop on Natural Language Processing and Computational Social Science. Vancouver, Canada: Association for Computational Linguistics, pp.7-16. 
 * Link to publication: [https://pdfs.semanticscholar.org/225f/f8a6a562bbb64b22cebfcd3288c6b930d1ef.pdf] (https://pdfs.semanticscholar.org/225f/f8a6a562bbb64b22cebfcd3288c6b930d1ef.pdf)* Link to data: https://github.com/AkshitaJha/NLP_CSS_2017 
 * Task description: Hierarchy of Sexism (Benevolent sexism, hostile sexism, none) 
 * Details of task: Sexism 
 * Size of dataset: 712 
 * Percentage abusive: 1 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Tweets were 'manually identified' by the authors to idenify the 712 tweets (not entirely sure what it means). Then, three 23-year old non-activist feminists validated the tweets. Seems like they did not remove any tweets after this. 
 * Annotation agreement: Fleiss' Kappa = 0.74 
  
 15. __Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (English)__
 * Reference: Fersini, E., Rosso, P. and Anzovino, M., 2018. Overview of the Task on Automatic Misogyny Identification at IberEval 2018. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 
 * Link to publication: [http://ceur-ws.org/Vol-2150/overview-AMI.pdf] (http://ceur-ws.org/Vol-2150/overview-AMI.pdf)* Link to data: https://amiibereval2018.wordpress.com/important-dates/data/ 
 * Task description: Binary (misogyny / not)
5 categories of misogyny (stereotype, dominance, derailing, sexual harassment, discredit)
Target of misogyny (active [individual directed] or passive [group directed]) 
 * Details of task: Sexism 
 * Size of dataset: 3977 
 * Percentage abusive: 0.47 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Crowdsourcing: CrowdFlower platform, 3 annotators per tweet. 
Gold standard, to test Crowdsource workers, created by two annotators annotating tweets & then an expert, 3rd annotator, intervening in cases of disagreement.
 
 * Annotation agreement: Not given 
  
 16. __CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English)__
 * Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 
 * Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf] (https://www.aclweb.org/anthology/P19-1271.pdf)* Link to data: https://github.com/marcoguerini/CONAN 
 * Task description: Binary (Islamophobic / not)
Then: multi-topic: Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic 
 * Details of task: Islamophobia 
 * Size of dataset: 1288 
 * Percentage abusive: 1 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Synthetic / Facebook 
 * Medium: Text 
 * Annotation process: 111 expert 'operators' from NGOs against hate speech, during 9 sessions (usually lasting 3 hours), created the synthetic posts 
 * Annotation agreement: Not relevant 
  
 17. __Characterizing and Detecting Hateful Users on Twitter__
 * Reference: Ribeiro, M., Calais, P., Santos, Y., Almeida, V. and Meira, W., 2018. Characterizing and Detecting Hateful Users on Twitter. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1803.08977.pdf] (https://arxiv.org/pdf/1803.08977.pdf)* Link to data: https://github.com/manoelhortaribeiro/HatefulUsersTwitter 
 * Task description: Binary (hateful/not).
No specific targets are focused on. The instructions given to annotators explicitly mention gender, religion and race as examples. 
 * Details of task: Hate per se 
 * Size of dataset: 4972 
 * Percentage abusive: 0.11 
 * Language: English 
 * Level of annotation: Users 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Annotators on CrowdFlower were asked to annotate each user profile, based on reviewing the' most recent 200 tweets.
Each user profile was annotated independently by 3 annotators. If there was any disagreement then up to 5 annotators were used. 
Annotators were given examples of terms and. codewords in ADL's hate symbol database (as training). 
 * Annotation agreement: Not given 
  
 18. __A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Gab)__
 * Reference: Qian, J., Bethke, A., Belding, E. and Yang Wang, W., 2019. A Benchmark Dataset for Learning to Intervene in Online Hate Speech. ArXiv,. 
 * Link to publication: [https://arxiv.org/abs/1909.04251] (https://arxiv.org/abs/1909.04251)* Link to data: https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech 
 * Task description: Binary (hateful/not). 
 * Details of task: Hate per se 
 * Size of dataset: 33776 
 * Percentage abusive: 0.43 
 * Language: English 
 * Level of annotation: Content (in the context of a conversation) 
 * Platform: Gab 
 * Medium: Text 
 * Annotation process: Annotators on Mechanical Turk.
2/3 agreement required to label a post as hate speech.
Excluding the rejected answers, the annotators were provided by 926 workers. 
 * Annotation agreement: Not given 
  
 19. __A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Reddit)__
 * Reference: Qian, J., Bethke, A., Belding, E. and Yang Wang, W., 2019. A Benchmark Dataset for Learning to Intervene in Online Hate Speech. ArXiv,. 
 * Link to publication: [https://arxiv.org/abs/1909.04251] (https://arxiv.org/abs/1909.04251)* Link to data: https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech 
 * Task description: Binary (hateful/not). 
 * Details of task: Hate per se 
 * Size of dataset: 22324 
 * Percentage abusive: 0.24 
 * Language: English 
 * Level of annotation: Posts - with context of the converstaional thread taken into account 
 * Platform: Reddit 
 * Medium: Text 
 * Annotation process: Annotators on Mechanical Turk.
2/3 agreement required to label a post as hate speech.
Excluding the rejected answers, the annotators were provided by 926 workers. 
 * Annotation agreement: Not given 
  
 20. __Multilingual and Multi-Aspect Hate Speech Analysis (English)__
 * Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 
 * Link to publication: [https://arxiv.org/abs/1908.11049] (https://arxiv.org/abs/1908.11049)* Link to data: https://github.com/HKUST-KnowComp/MLMA_hate_speech 
 * Task description: Detailed taxonomy with cross-cutting attributes:
HOSTILITY (Abusive, Hateful, Offensive, Disrespectful, Fearful, Normal)
DIRECTNESS (Direct/indirect)
Target attribute (Origin [covers race, ethnicity and nationality], Gender, Sexual Orientation, Religion, Disability, Other)
Target Group (16 identified, of which the five most common are: Individual, Other, Women, Special needs, African Descent)
Annotator sentiment [i.e. how the annotators felt on seeing the tweet] (Disgust, Shock, Anger, Sadness, Fear, Confusion, Indifference) 
 * Details of task: Gender, Sexual orientation, Religion, Disability 
 * Size of dataset: 5647 
 * Percentage abusive: 0.76 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Annotators on Mechanical Turk.
5 annotators per entry, with majority voting to decide final labels.
For the more subjetive labels, all of the annotations were retained(i.e. hostility type and the annotator’s sentiment labels).
Annotators were provided with definitions of offensive words from Urban Dictionary.
Annotators were reminded 'not to let their personal opinions about the topics being discussed in the tweets influence their annotation decisions'.
 
 * Annotation agreement: Krippendorf score: 0.153 
  
 21. __Exploring Hate Speech Detection in Multimodal Publications__
 * Reference: Gomez, R., Gibert, J., Gomez, L. and Karatzas, D., 2019. Exploring Hate Speech Detection in Multimodal Publications. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1910.03814.pdf] (https://arxiv.org/pdf/1910.03814.pdf)* Link to data: https://gombru.github.io/2019/10/09/MMHS/ 
 * Task description: Six primary categories (No attacks to any community, Racist, Sexist, Homophobic, Religion based attack, Attack to other community. 
 * Details of task: Racism, Sexism, Homophobia, Religion-based attack 
 * Size of dataset: 149823 
 * Percentage abusive: 0.25 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text and Images/Memes 
 * Annotation process: Annotators on Mechanical Turk.
3 annotators per entry, with majority voting (2/3) to decide final labels. 
 * Annotation agreement: Not given 
  
 22. __Predicting the Type and Target of Offensive Posts in Social Media__
 * Reference: Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N. and Kumar, R., 2019. SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval). ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1902.09666.pdf
https://arxiv.org/pdf/1903.08983.pdf] (https://arxiv.org/pdf/1902.09666.pdf
https://arxiv.org/pdf/1903.08983.pdf)* Link to data: http://competitions.codalab.org/ competitions/20011 
 * Task description: Branching structure of tasks:
Binary (Offensive, Not)
Within Offensive (Target, Not)
Within Target (Individual, Group, Other) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 14100 
 * Percentage abusive: 0.33 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: First, 6 experts annotated 300 samples to create a gold standard dataset.
Then, crowdsourcing (Figure 8) used. 2 annotations were requested per tweet and, in cases of disagreement, a 3rd was then used.
Quality controls were used 
 * Annotation agreement: 60% of the time, the 2 F8 annotators were in 100% agreement 
  
 23. __hatEval, SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter (English)__
 * Reference: Basile, V., Bosco, C., Fersini, E., Nozza, D., Patti, V., Pardo, F., Rosso, P. and Sanguinetti, M., 2019. SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter. In: Proceedings of the 13th International Workshop on Semantic Evaluation. Minneapolis, Minnesota: Association for Computational Linguistics, pp.54-63. 
 * Link to publication: [https://www.aclweb.org/anthology/S19-2007] (https://www.aclweb.org/anthology/S19-2007)* Link to data: competitions.codalab.org/competitions/19935
https://github.com/msang/hateval/blob/master/annotation_guidelines.md  
 * Task description: Branching structure of tasks:
Binary (Hate, Not)
Within Hate (Group, Individual)
Within Hate (Agressive, Not) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 13000 
 * Percentage abusive: 0.4 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Combination of experts and crowdsourcing.
First, Crowdsourcing: Annotators were give guidelines. 3 independent judgments per tweet. Majority label adopted.
Second, Expert: 2 experts redo annotations. Majority decision taken, using the crowdsource input as a 3rd judgement. 
 
 * Annotation agreement: Average confidence' used (which combines both agreement and reliability of each contributor):
English: 0.83, 0.70, 0.73 
  
 24. __Peer to Peer Hate: Hate Speech Instigators and Their Targets__
 * Reference: ElSherief, M., Nilizadeh, S., Nguyen, D., Vigna, G. and Belding, E., 2018. Peer to Peer Hate: Hate Speech Instigators and Their Targets. In: Proceedings of the Twelfth International AAAI Conference on Web and Social Media (ICWSM 2018). Santa Barbara, California: University of California, pp.52-61. 
 * Link to publication: [https://aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/view/17905/16996] (https://aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/view/17905/16996)* Link to data: https://github.com/mayelsherif/hate_speech_icwsm18 
 * Task description: Binary (Hate/Not), only for tweets which have both a Hate Instigator and Hate Target (introducing an interpersonal dimension) 
 * Details of task: Hate per se 
 * Size of dataset: 27330 
 * Percentage abusive: 0.98 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Annotators on CrowdFlower.
3 annotators per entry, with majority voting (2/3) to decide final labels. 
 * Annotation agreement: 92.8% argreeement for hateful/not.
82.6% agreement for whether targetted at a person.
 
  
 25. __Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages__
 * Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 
 * Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true] (https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)* Link to data: https://hasocfire.github.io/hasoc/2019/dataset.html 
 * Task description: A: Hate / Offensive or neither;
B: Hatespeech, Offensive, or Profane;
C: Targeted or Untargeted 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 7005 
 * Percentage abusive: 0.36 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter and Facebook 
 * Medium: Text 
 * Annotation process: Students 
 * Annotation agreement: 72.00% 
  
 26. __Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior__
 * Reference: Founta, A., Djouvas, C., Chatzakou, D., Leontiadis, I., Blackburn, J., Stringhini, G., Vakali, A., Sirivianos, M. and Kourtellis, N., 2018. Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1802.00393.pdf] (https://arxiv.org/pdf/1802.00393.pdf)* Link to data: https://dataverse.mpi-sws.org/dataset.xhtml?persistentId=doi:10.5072/FK2/ZDTEMN 
 * Task description: Multi-thematic (Abusive, Hateful, Normal, Spam) 
 * Details of task: Hate per se 
 * Size of dataset: 80000 
 * Percentage abusive: 0.18 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Very detailed information is given: multiple rounds, using a smaller 300 tweet dataset for testing the schema. For the final 80k, 5 judgements per tweet. CrowdFlower 
 * Annotation agreement: 55.9% = 4/5, 36.6% = 3/5, 7.5% = 2/5 
  
 27. __A Large Labeled Corpus for Online Harassment Research__
 * Reference: Golbeck, J., Ashktorab, Z., Banjo, R., Berlinger, A., Bhagwan, S., Buntain, C., Cheakalos, P., Geller, A., Gergory, Q., Gnanasekaran, R., Gnanasekaran, R., Hoffman, K., Hottle, J., Jienjitlert, V., Khare, S., Lau, R., Martindale, M., Naik, S., Nixon, H., Ramachandran, P., Rogers, K., Rogers, L., Sarin, M., Shahane, G., Thanki, J., Vengataraman, P., Wan, Z. and Wu, D., 2017. A Large Labeled Corpus for Online Harassment Research. In: Proceedings of the 2017 ACM on Web Science Conference. New York: Association for Computing Machinery, pp.229-233. 
 * Link to publication: [http://www.cs.umd.edu/~golbeck/papers/trolling.pdf] (http://www.cs.umd.edu/~golbeck/papers/trolling.pdf)* Link to data: jgolbeck@umd.edu 
 * Task description: Binary (harassment/not) 
 * Details of task: Person-directed 
 * Size of dataset: 35000 
 * Percentage abusive: 0.16 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 35,000 collected. Each tweet annotated by two coders. Then, in cases of disagreement a 3rd coder was brought in to abjudicate. 2,711 tweets required a 3rd coder.  
 * Annotation agreement: Cohen's Kappa: 0.84 
  
 28. __Ex Machina: Personal Attacks Seen at Scale, Personal attacks__
 * Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1610.08914] (https://arxiv.org/pdf/1610.08914)* Link to data: https://github.com/ewulczyn/wiki-detox 
 * Task description: Binary (Personal attack, Not) 
 * Details of task: Person-directed 
 * Size of dataset: 115737 
 * Percentage abusive: 0.12 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Wikipedia 
 * Medium: Text 
 * Annotation process: Each comment was annotated by 10 annotators. The majority decision was taken. Based on Crowdflower annotations. Annotators with 70% accuracy or less were removed, resulting in worse 2% of annotators being removed. 
 * Annotation agreement: 0.45 Krippendorf Alpha 
  
 29. __Ex Machina: Personal Attacks Seen at Scale, Toxicity__
 * Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1610.08914] (https://arxiv.org/pdf/1610.08914)* Link to data: https://meta.wikimedia.org/wiki/Research:Detox/Data_Release#Schema_for_{attack/aggression/toxicity}_worker_demographics.tsv 
 * Task description: Toxicity/healthiness judgement 5 points (-2 == very toxic, 0 == neutral, 2 == very heallthy) 
 * Details of task: Person-directed 
 * Size of dataset: 100000 
 * Percentage abusive: NA 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Wikipedia 
 * Medium: Text 
 * Annotation process: Each comment was annotated by 10 annotators. The majority decision was taken. Based on Crowdflower annotations. Annotators with 70% accuracy or less were removed, resulting in worse 2% of annotators being removed. 
 * Annotation agreement: / 
  
 30. __Detecting cyberbullying in online communities (World of Warcraft)__
 * Reference: Bretschneider, U. and Peters, R., 2016. Detecting Cyberbullying in Online Communities. Research Papers, 61. 
 * Link to publication: [http://aisel.aisnet.org/ecis2016_rp/61/] (http://aisel.aisnet.org/ecis2016_rp/61/)* Link to data: http://ub-web.de/research/ 
 * Task description: Binary (Harassment, Not) 
 * Details of task: Person-directed 
 * Size of dataset: 16975 
 * Percentage abusive: 0.01 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: World of Warcraft 
 * Medium: Text 
 * Annotation process: 3 human experts for each post; only cases with 2/3 or 3/3 agreement are included 
 * Annotation agreement: 0.51 Fleiss Kappa - only calculated on posts which at least one annotator annotated as offensive 
  
 31. __Detecting cyberbullying in online communities (League of Legends)__
 * Reference: Bretschneider, U. and Peters, R., 2016. Detecting Cyberbullying in Online Communities. Research Papers, 61. 
 * Link to publication: [http://aisel.aisnet.org/ecis2016_rp/61/] (http://aisel.aisnet.org/ecis2016_rp/61/)* Link to data: http://ub-web.de/research/ 
 * Task description: Binary (Harassment, Not) 
 * Details of task: Person-directed 
 * Size of dataset: 17354 
 * Percentage abusive: 0.01 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: League of Legends 
 * Medium: Text 
 * Annotation process: 3 human experts for each post; only cases with 2/3 or 3/3 agreement are included 
 * Annotation agreement: 0.72 Fleiss Kappa - only calculated on posts which at least one annotator annotated as offensive
 
  
 32. __A Quality Type-aware Annotated Corpus and Lexicon for Harassment Research__
 * Reference: Rezvan, M., Shekarpour, S., Balasuriya, L., Thirunarayan, K., Shalin, V. and Sheth, A., 2018. A Quality Type-aware Annotated Corpus and Lexicon for Harassment Research. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1802.09416.pdf] (https://arxiv.org/pdf/1802.09416.pdf)* Link to data: https://github.com/Mrezvan94/Harassment-Corpus 
 * Task description: 5-topic (Sexual, Racist, Appearance-related, Intellectual, Political) 
 * Details of task: Racism, Sexism, Appearance-related, intellectual, political 
 * Size of dataset: 24189 
 * Percentage abusive: 0.13 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 3 native English experts per tweet 
 * Annotation agreement: Cohen's Kappa: Sexual (0.70), Racial (0.84), Appearance-related (1.00), Intellectual (0.80), Political (0.69) 
  
 33. __Ex Machina: Personal Attacks Seen at Scale, Aggression and Friendliness__
 * Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1610.08914] (https://arxiv.org/pdf/1610.08914)* Link to data: https://meta.wikimedia.org/wiki/Research:Detox/Data_Release#Schema_for_{attack/aggression/toxicity}_worker_demographics.tsv 
 * Task description: Aggression/friendliness judgement on a 5 point scale. (-2 == very aggressive, 0 == neutral, 3 == very friendly). Aggression also includes 'passive aggression'. 
 * Details of task: Person-Directed + Group-Directed 
 * Size of dataset: 160000 
 * Percentage abusive: NA 
 * Language: English 
 * Level of annotation: Posts 
 * Platform: Wikipedia 
 * Medium: Text 
 * Annotation process: Each comment was annotated by 10 annotators. The majority decision was taken. Based on Crowdflower annotations. Annotators with 70% accuracy or less were removed, resulting in worse 2% of annotators being removed. 
 * Annotation agreement: / 


### French
 34. __CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (French)__
 * Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 
 * Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf] (https://www.aclweb.org/anthology/P19-1271.pdf)* Link to data: https://github.com/marcoguerini/CONAN 
 * Task description: Binary (Islamophobic / not)
Then: multi-topic: Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic 
 * Details of task: Islamophobia 
 * Size of dataset: 1719 
 * Percentage abusive: 1 
 * Language: French 
 * Level of annotation: Posts 
 * Platform: Synthetic / Facebook 
 * Medium: Text 
 * Annotation process: 111 expert 'operators' from NGOs against hate speech, during 9 sessions (usually lasting 3 hours), created the synthetic posts 
 * Annotation agreement: Not relevant 
  
 35. __Multilingual and Multi-Aspect Hate Speech Analysis (French)__
 * Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 
 * Link to publication: [https://arxiv.org/abs/1908.11049] (https://arxiv.org/abs/1908.11049)* Link to data: https://github.com/HKUST-KnowComp/MLMA_hate_speech 
 * Task description: Detailed taxonomy with cross-cutting attributes:
HOSTILITY (Abusive, Hateful, Offensive, Disrespectful, Fearful, Normal)
DIRECTNESS (Direct/indirect)
Target attribute (Origin [covers race, ethnicity and nationality], Gender, Sexual Orientation, Religion, Disability, Other)
Target Group (16 identified, of which the five most common are: Individual, Other, Women, Special needs, African Descent)
Annotator sentiment [i.e. how the annotators felt on seeing the tweet] (Disgust, Shock, Anger, Sadness, Fear, Confusion, Indifference) 
 * Details of task: Gender, Sexual orientation, Religion, Disability 
 * Size of dataset: 4014 
 * Percentage abusive: 0.72 
 * Language: French 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Annotators on Mechanical Turk.
5 annotators per entry, with majority voting to decide final labels.
For the more subjetive labels, all of the annotations were retained(i.e. hostility type and the annotator’s sentiment labels).
Annotators were provided with definitions of offensive words from Urban Dictionary.
Annotators were reminded 'not to let their personal opinions about the topics being discussed in the tweets influence their annotation decisions'.
 
 * Annotation agreement: Krippendorf score: 0.244 


### German
 36. __Measuring the Reliability of Hate Speech Annotations: The Case of the European Refugee Crisis__
 * Reference: Ross, B., Rist, M., Carbonell, G., Cabrera, B., Kurowsky, N. and Wojatzki, M., 2017. Measuring the Reliability of Hate Speech Annotations: The Case of the European Refugee Crisis. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1701.08118.pdf] (https://arxiv.org/pdf/1701.08118.pdf)* Link to data: https://github.com/UCSM-DUE/IWG_hatespeech_public 
 * Task description: Binary (Anti-refugee hate, None) 
 * Details of task: Refugees 
 * Size of dataset: 469 
 * Percentage abusive: NA 
 * Language: German 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 2 annotations per tweet, from six expert annotators. Then, the second expert gives each tweet a rating based on a 6-point Likert scale (1 = Not offensive at all, 6 = Very offensive) 
 * Annotation agreement: Krippendorf alpha = 0.38 (hate/not) 
 
 37. __Detecting Offensive Statements Towards Foreigners in Social Media__
 * Reference: Bretschneider, U. and Peters, R., 2017. Detecting Offensive Statements towards Foreigners in Social Media. In: Proceedings of the 50th Hawaii International Conference on System Sciences. 
 * Link to publication: [https://pdfs.semanticscholar.org/23dc/df7c7e82807445afd9f19474fc0a3d8169fe.pdf] (https://pdfs.semanticscholar.org/23dc/df7c7e82807445afd9f19474fc0a3d8169fe.pdf)* Link to data: http://ub-web.de/research/ 
 * Task description: Hierarchical (Anti-foreigner prejudice: (1) slightly offensive/offensive and (2) explicitly/substantially offensive).
6-targets: Foreigner, Government, Press, Community, Other, Unknown 
 * Details of task: Anti-foreigner prejudice 
 * Size of dataset: 5836 
 * Percentage abusive: 0.11 
 * Language: German 
 * Level of annotation: Posts 
 * Platform: Facebook 
 * Medium: Text 
 * Annotation process: 2 expert annotators. A 'consensus' annotation is computed. 
 * Annotation agreement: Cohens Kappa = 0.78, 0.73 and 068 across the 3 pages - only calculated on posts which at least one annotator annotated as offensive 
  
 38. __GermEval 2018__
 * Reference: Wiegand, M., Siegel, M. and Ruppenhofer, J., 2018. Overview of the GermEval 2018 Shared Task on the Identification of Offensive Language. In: Proceedings of GermEval 2018, 14th Conference on Natural Language Processing (KONVENS 2018). Vienna, Austria: Research Gate. 
 * Link to publication: [https://www.researchgate.net/publication/327914386_Overview_of_the_GermEval_2018_Shared_Task_on_the_Identification_of_Offensive_Language] (https://www.researchgate.net/publication/327914386_Overview_of_the_GermEval_2018_Shared_Task_on_the_Identification_of_Offensive_Language)* Link to data: https://github.com/uds-lsv/GermEval-2018-Data 
 * Task description: Branching structure:
Binary (Offense, Other)
3-levels within Offense (Abuse, Insult, Profanity) 
 * Details of task: Group-directed + incivility 
 * Size of dataset: 8541 
 * Percentage abusive: 0.34 
 * Language: German 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: After testing on 240 tweets, each tweet was annotated by one of the 3 experts. Very unusual strategy.  
 * Annotation agreement: Tested on 240 tweets; 3 annotators. Fleiss' Kappa = 0.66. 
 
 39. __Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages__
 * Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 
 * Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true] (https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)* Link to data: https://hasocfire.github.io/hasoc/2019/dataset.html 
 * Task description: A: Hate / Offensive or neither;
B: Hatespeech, Offensive, or Profane 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 4669 
 * Percentage abusive: 0.24 
 * Language: German 
 * Level of annotation: Posts 
 * Platform: Twitter and Facebook 
 * Medium: Text 
 * Annotation process: Students 
 * Annotation agreement: 96% 
 
 
 ### Greek
 40. __Deep Learning for User Comment Moderation, Flagged Comments__
 * Reference: Pavlopoulos, J., Malakasiotis, P. and Androutsopoulos, I., 2017. Deep Learning for User Comment Moderation. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.25-35. 
 * Link to publication: [https://www.aclweb.org/anthology/W17-3004
https://www.aclweb.org/anthology/D17-1117] (https://www.aclweb.org/anthology/W17-3004
https://www.aclweb.org/anthology/D17-1117)* Link to data: http://www.straintek.com/data/ 
 * Task description: Binary (Flagged, Not) 
 * Details of task: Flagged content 
 * Size of dataset: 1450000 
 * Percentage abusive: 0.34 
 * Language: Greek 
 * Level of annotation: Posts 
 * Platform: Gazetta 
 * Medium: text 
 * Annotation process: Flagged by moderators - 2 professionals + occasional journalist help 
 * Annotation agreement: Not reported; most likely not tested 
  
 41. __Deep Learning for User Comment Moderation, Moderated Comments__
 * Reference: Pavlopoulos, J., Malakasiotis, P. and Androutsopoulos, I., 2017. Deep Learning for User Comment Moderation. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.25-35. 
 * Link to publication: [https://www.aclweb.org/anthology/W17-3004
https://www.aclweb.org/anthology/D17-1117] (https://www.aclweb.org/anthology/W17-3004
https://www.aclweb.org/anthology/D17-1117)* Link to data: http://www.straintek.com/data/ 
 * Task description: Binary (Flagged, Not) 
 * Details of task: Flagged content 
 * Size of dataset: 1500 
 * Percentage abusive: 0.22 
 * Language: Greek 
 * Level of annotation: Posts 
 * Platform: Gazetta 
 * Medium: text 
 * Annotation process: 5 annotators re-annotated the dataset 
 * Annotation agreement: 0.4762 Krippendorf Alpha
0.4749 mean pairwise Cohen's Kappa
81.33% average pairwise agreement 
  
 42. __Offensive Language Identification in Greek__
 * Reference: Pitenis, Z., Zampieri, M. and Ranasinghe, T., 2020. Offensive Language Identification in Greek. ArXiv. 
 * Link to publication: [https://arxiv.org/pdf/2003.07459v1.pdf] (https://arxiv.org/pdf/2003.07459v1.pdf)* Link to data: https://sites.google.com/site/offensevalsharedtask/home 
 * Task description: Branching structure of tasks:
Binary (Offensive, Not)
Within Offensive (Target, Not)
Within Target (Individual, Group, Other) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 4779 
 * Percentage abusive: 0.29 
 * Language: Greek 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Three volunteers, pairwise comparisons 
 * Annotation agreement: unclear 
 
 
 ### Hindi-English
 43. __Aggression-annotated Corpus of Hindi-English Code-mixed Data__
 * Reference: Kumar, R., Reganti, A., Bhatia, A. and Maheshwari, T., 2018. Aggression-annotated Corpus of Hindi-English Code-mixed Data. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1803.09402] (https://arxiv.org/pdf/1803.09402)* Link to data: https://github.com/kraiyani/Facebook-Post-Aggression-Identification 
 * Task description: 3-part hierachy for hate (None, Covert Aggression, Overt Aggression) & 4-part target categorisation (Physical threat, Sexual threat, Identity threat, Non-threatening aggression) & 3-part discursive role categorisation (Attack, Defend, Abet) 
 * Details of task: Numerous sub-categorizations 
 * Size of dataset: 18000 
 * Percentage abusive: 0.06 
 * Language: Hindi-English 
 * Level of annotation: Posts 
 * Platform: Facebook 
 * Medium: Text 
 * Annotation process: 
The actual work (~40k comments) was done by 4 expert annotators (PhD students in Linguistics) - native Hindi + native-like English competence.
Testing of the annotation taxaonomy was done on CF and with experts. 
 * Annotation agreement: Using CrowdFlower, each tweet was annotated by 3 annotators (77 annotators took part in total). Testing was conducted on 1,100 test instances. 72% agreement for (Overt/Covert/None) and for the other categories (10-classes), agreement was 57%. 
  
 44. __Aggression-annotated Corpus of Hindi-English Code-mixed Data__
 * Reference: Kumar, R., Reganti, A., Bhatia, A. and Maheshwari, T., 2018. Aggression-annotated Corpus of Hindi-English Code-mixed Data. ArXiv,. 
 * Link to publication: [https://arxiv.org/pdf/1803.09402] (https://arxiv.org/pdf/1803.09402)* Link to data: https://github.com/kraiyani/Facebook-Post-Aggression-Identification 
 * Task description: 3-part hierachy for hate (None, Covert Aggression, Overt Aggression) & 4-part target (Physical threat, Sexual threat, Identity threat, Non-threatening aggression) & 3-part discursive roles (Attack, Defend, Abet) 
 * Details of task: Numerous sub-categorizations 
 * Size of dataset: 21000 
 * Percentage abusive: 0.27 
 * Language: Hindi-English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 
The actual work (~40k comments) was done by 4 expert annotators (PhD students in Linguistics) - native Hindi + native-like English competence.
Testing of the annotation taxaonomy was done on CF and with experts. 
 * Annotation agreement: Using CrowdFlower, each tweet was annotated by 3 annotators (77 annotators took part in total). Testing was conducted on 1,100 test instances. 72% agreement for (Overt/Covert/None) and for the other categories (10-classes), agreement was 57%. 
  
 45. __Did You Offend Me? Classification of Offensive Tweets in Hinglish Language__
 * Reference: Mathur, P., Sawhney, R., Ayyar, M. and Shah, R., 2018. Did you offend me? Classification of Offensive Tweets in Hinglish Language. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.138-148. 
 * Link to publication: [https://www.aclweb.org/anthology/W18-5118] (https://www.aclweb.org/anthology/W18-5118)* Link to data: https://github.com/pmathur5k10/Hinglish-Offensive-Text-Classification 
 * Task description: Hierarchy (Not Offensive, Abusive, Hate) 
 * Details of task: Sexism 
 * Size of dataset: 3189 
 * Percentage abusive: 0.65 
 * Language: Hindi-English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 3 experts in NLP annotated all of the tweets. Majority decision (2/3 accepted). In case of disagreement (i.e. all 3 pick something different), additiional expert make the decision - this happened in 386 tweets. 
 * Annotation agreement: average Cohen's kappa = 0.83 
  
 46. __A Dataset of Hindi-English Code-Mixed Social Media Text for Hate Speech Detection__
 * Reference: Bohra, A., Vijay, D., Singh, V., Sarfaraz Akhtar, S. and Shrivastava, M., 2018. A Dataset of Hindi-English Code-Mixed Social Media Text for Hate Speech Detection. In: Proceedings of the Second Workshop on Computational Modeling of People’s Opinions, Personality, and Emotions in Social Media. New Orleans, Louisiana: Association for Computational Linguistics, pp.36-41. 
 * Link to publication: [https://www.aclweb.org/anthology/W18-1105] (https://www.aclweb.org/anthology/W18-1105)* Link to data: https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text 
 * Task description: Binary (Hate, Not) 
 * Details of task: Hate per se 
 * Size of dataset: 4575 
 * Percentage abusive: 0.36 
 * Language: Hindi-English 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 2 expert annotators with experience in Hindi and English. They were given a set of 50 tweets (25 hate and 25 non hate) to make their annotations. 
 * Annotation agreement: Kappa = 0.982 
  
 47. __Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages__
 * Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 
 * Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true] (https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)* Link to data: https://hasocfire.github.io/hasoc/2019/dataset.html 
 * Task description: A: Hate / Offensive or neither;
B: Hatespeech, Offensive, or Profane;
C: Targeted or Untargeted 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 5983 
 * Percentage abusive: 0.51 
 * Language: Hindi 
 * Level of annotation: Posts 
 * Platform: Twitter and Facebook 
 * Medium: Text 
 * Annotation process: Students 
 * Annotation agreement: 83% 
 
 
 ### Indonesian
 48. __Hate Speech Detection in the Indonesian Language: A Dataset and Preliminary Study__
 * Reference: Alfina, I., Mulia, R., Fanany, M. and Ekanata, Y., 2017. Hate Speech Detection in the Indonesian Language: A Dataset and Preliminary Study. In: International Conference on Advanced Computer Science and Information Systems. pp.233-238. 
 * Link to publication: [https://ieeexplore.ieee.org/document/8355039] (https://ieeexplore.ieee.org/document/8355039)* Link to data: https://github.com/ialfina/id-hatespeech-detection 
 * Task description: Binary (Hate, Not) 
 * Details of task: Hate per se 
 * Size of dataset: 713 
 * Percentage abusive: 0.36 
 * Language: Indonesian 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 3 annotators per tweet from a team of 30 volunteers.
22 sets of 50 tweets created; each set was annotated by different teams, with diverse members (based on religious, racial and gender backgrounds).
Annotators trained to ensure they understand the definition of hate speech that they were given.
Only 100% agreement tweets retained. This reduced the size from 1,100 tweets to 713 
 * Annotation agreement: 64.8% of tweets there was 100% agreement 
  
 49. __Multi-Label Hate Speech and Abusive Language Detection in Indonesian Twitter__
 * Reference: Okky Ibrohim, M. and Budi, I., 2019. Multi-label Hate Speech and Abusive Language Detection in Indonesian Twitter. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.46-57. 
 * Link to publication: [https://www.aclweb.org/anthology/W19-3506] (https://www.aclweb.org/anthology/W19-3506)* Link to data: https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection 
 * Task description: Four-levels (No hate speech, no hate speech but abusive, hate speech but no abuse, hate speech and abuse)
Within hate there are 5 categories (content can be split into multiple of the first four): (1) Religion/creed, (2) Race/ethnicity, (3) Physical/disability, (4) Gender/sexual orientation, (5) Other invective/slander
Within hate there are also 5 strengths: Weak, Moderate and Strong 
 * Details of task: Religion, Race, Diab 
 * Size of dataset: 13169 
 * Percentage abusive: 0.42 
 * Language: Indonesian 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Crowdsourcing, implemented in two phases.
First: annotate whether tweets are hate/abuse or not
Second: annotate for target, categories and levels.
30 crowdsourced annotators used in total. 3 annotators per tweet.
Only 100% agreement retained for the binary task.
Majority decision (2/3) used for the second task.
Gold standard questions were created by a trained linguist.
 
 * Annotation agreement: Binary decisions (hate speech/abusive or not): 68.44% - 11,292 out of 16,500 tweets (originally collected + harvested from prior datasets) have 100% agreement
Second task (Categories + strengths): 97.56% have either 2/3 agreement or 100% (139 are removed when disagreement is greater than this) 
  
 50. __A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media__
 * Reference: Ibrohim, M. and Budi, I., 2018. A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media. Procedia Computer Science, 135, pp.222-229. 
 * Link to publication: [https://www.sciencedirect.com/science/article/pii/S1877050918314583] (https://www.sciencedirect.com/science/article/pii/S1877050918314583)* Link to data: https://github.com/okkyibrohim/id-abusive-language-detection 
 * Task description: Hierarchical (Not abusive, Abusive but not offensive, Offensive) 
 * Details of task: Incivility 
 * Size of dataset: 2016 
 * Percentage abusive: 0.54 
 * Language: Indonesian 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Each tweet was labelled by 3 people. There were 20 volunteer annotators - 'To ensure that annotators understand for they task, we make an annotation guide and explaining that annotation guide to the annotators' (p. 226) 
 * Annotation agreement: Only 100% retained; in 80.6% of cases there was 100% agreement 
 
 
 ### Italian
 51. __An Italian Twitter Corpus of Hate Speech against Immigrants__
 * Reference: Sanguinetti, M., Poletto, F., Bosco, C., Patti, V. and Stranisci, M., 2018. An Italian Twitter Corpus of Hate Speech against Immigrants. In: Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018). Miyazaki, Japan: European Language Resources Association (ELRA). 
 * Link to publication: [https://www.aclweb.org/anthology/L18-1443] (https://www.aclweb.org/anthology/L18-1443)* Link to data: https://github.com/msang/hate-speech-corpus 
 * Task description: Binary target: Immigrants, Roma and Muslims [combined]. AND Multi-thematic categories are identified. Hate is also measured by intensity, making it hiearchical (Hate: no/yes, Aggressiveness: no/weak/strong, Offensiveness: no/weak/strong, Irony: no/yes, Stereotype: no/yes, Incitement degree: 0-4) 
 * Details of task: Immigrants, Roma and Muslims 
 * Size of dataset: 1827 
 * Percentage abusive: 0.13 
 * Language: Italian 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 3,154 annotated by experts (2 per tweet) and then 2,855 annotated by CF (3+ per tweet). Crowdflower annotators are assessed for minimum reliability (65% required) - five annotators did more than 90% of the work 
 * Annotation agreement: Experts (Cohen's K): hs (0.45), aggression (0.45), irony (0.32), stereotypes (0.41), intensity (0.21)
CF (Krippendorf's Alpha): hs (0.38), aggression (0.25), irony (0.12), stereotypes (0.20), intensity (0.31) 
  
 52. __Overview of the EVALITA 2018 Hate Speech Detection Task (Facebook)__
 * Reference: Bosco, C., Dell'Orletta, F. and Poletto, F., 2018. Overview of the EVALITA 2018 Hate Speech Detection Task. In: EVALITA 2018-Sixth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. CEUR, pp.1-9. 
 * Link to publication: [http://ceur-ws.org/Vol-2263/paper010.pdf] (http://ceur-ws.org/Vol-2263/paper010.pdf)* Link to data: http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html 
 * Task description: Binary (Hate / not)

Other variables, not used in the competition but described in the data:

Within hate for FACEBOOK only: (1) No hate, (2) Weak Hate, (3) Strong Hate
Within hate for FACEBOOK only: (1) religion, (2) physical and/or mental handicap, (3) socio-economic status, (4) politics, (5) race, (6) sex and gender, (7) Other 
 * Details of task: Religion, physical and/or mental handicap, socio-economic status, politics, race, sex and gender 
 * Size of dataset: 4000 
 * Percentage abusive: 0.51 
 * Language: Italian 
 * Level of annotation: Posts 
 * Platform: Facebook 
 * Medium: Text 
 * Annotation process: Facebook:
5 bachelor students annotated comments.
3,865 received at least 3 annotations. 
 * Annotation agreement: Not given 
  
 53. __Overview of the EVALITA 2018 Hate Speech Detection Task (Twitter)__
 * Reference: Bosco, C., Dell'Orletta, F. and Poletto, F., 2018. Overview of the EVALITA 2018 Hate Speech Detection Task. In: EVALITA 2018-Sixth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. CEUR, pp.1-9. 
 * Link to publication: [http://ceur-ws.org/Vol-2263/paper010.pdf] (http://ceur-ws.org/Vol-2263/paper010.pdf)* Link to data: http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html 
 * Task description: Binary (Hate / not)

Other variables, not used in the competition but described in the data:

Within hate for TWITTER only: 1-4 rating of intensity
Within hate for TWITTER only: Aggressiveness (no, weak, strong), Offensiveness (no, weak, strong), Irony (yes, no) 
 * Details of task: Group-directed 
 * Size of dataset: 4000 
 * Percentage abusive: 0.32 
 * Language: Italian 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: 
Twitter:
Mix of Crowdflower and experts (the breakdown between the two is not explained) 
 * Annotation agreement: Not given 
  
 54. __CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (Italian)__
 * Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 
 * Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf] (https://www.aclweb.org/anthology/P19-1271.pdf)* Link to data: https://github.com/marcoguerini/CONAN 
 * Task description: Binary (Islamophobic / not)
Then: multi-topic: Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic 
 * Details of task: Islamophobia 
 * Size of dataset: 1071 
 * Percentage abusive: 1 
 * Language: Italian 
 * Level of annotation: Posts 
 * Platform: Synthetic / Facebook 
 * Medium: Text 
 * Annotation process: 111 expert 'operators' from NGOs against hate speech, during 9 sessions (usually lasting 3 hours), created the synthetic posts 
 * Annotation agreement: Not relevant 
  
 55. __Creating a WhatsApp Dataset to Study Pre-teen Cyberbullying__
 * Reference: Sprugnoli, R., Menini, S., Tonelli, S., Oncini, F. and Piras, E., 2018. Creating a WhatsApp Dataset to Study Pre-teen Cyberbullying. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2) Month: October. Brussels, Belgium: Association for Computational Linguistics, pp.51-59. 
 * Link to publication: [https://www.aclweb.org/anthology/W18-5107] (https://www.aclweb.org/anthology/W18-5107)* Link to data: https://github.com/dhfbk/WhatsApp-Dataset 
 * Task description: Binary (Cyberbullying, Not) 
 * Details of task: Person-directed 
 * Size of dataset: 14600 
 * Percentage abusive: 0.08 
 * Language: Italian 
 * Level of annotation: Posts, structured into 10 chats, with token level information 
 * Platform: Synthetic / Whatsapp 
 * Medium: Text 
 * Annotation process: The chats were developed synthetically, by children using Whatsapp as a form of role-play (each given roles with one researcher as the victim). Then, they were annotated by the researchers. 
 * Annotation agreement: Dice coefficient: 0.8 (based on one chat of 1,000 tokens) 
 
 
 ### Polish
 56. __Results of the PolEval 2019 Shared Task 6:First Dataset and Open Shared Task for Automatic Cyberbullying Detection in Polish Twitter__
 * Reference: Ogrodniczuk, M. and Kobyliński, L., 2019. Results of the PolEval 2019 Shared Task 6: First Dataset and Open Shared Task for Automatic Cyberbullying Detection in Polish Twitter. In: Proceedings of the PolEval 2019 Workshop. Warszawa: Institute of Computer Science, Polish Academy of Sciences. 
 * Link to publication: [http://poleval.pl/files/poleval2019.pdf] (http://poleval.pl/files/poleval2019.pdf)* Link to data: http://poleval.pl/tasks/task6 
 * Task description: Harmfulness score, three values;
Multilabel from seven phenomena;
Specific phrase in the text conveying the phenomena/om 
 * Details of task: Person-directed 
 * Size of dataset: 10041 
 * Percentage abusive: 0.09 
 * Language: Polish 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Two annotators label each doc, mixture of annotators, ties broken by senior annotator 
 * Annotation agreement: 0.9138 
  
 
 ### Portugese
 57. __A Hiierarchically-Labeled Portugese Hate Speech Dataset__
 * Reference: Fortuna, P., Rocha da Silva, J., Soler-Company, J., Warner, L. and Nunes, S., 2019. A Hierarchically-Labeled Portuguese Hate Speech Dataset. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.94-104. 
 * Link to publication: [https://www.aclweb.org/anthology/W19-3510] (https://www.aclweb.org/anthology/W19-3510)* Link to data: https://rdm.inesctec.pt/dataset/cs-2017-008 
 * Task description: Binary (Hate, Not)
Multi-level (81 categories, identified inductively; categories have different granularities and content ncan be assigned to multiple categories at once) 
 * Details of task: Multiple identities inductively categorized 
 * Size of dataset: 3059 
 * Percentage abusive: 0.32 
 * Language: Portugese 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Binary: Every tweet was annotated by 3 annotators (From a team of 18 annotators).
Note: annotators used their opinion to make judgements.
Majority vote taken for assignments
Hierarchy: one researcher annotated the corpus. Then, 500 tweets were checked by another to calculate IRR 
 * Annotation agreement: Binary, Fleiss' Kappa = 0.17
Hierarchy, Cohen's Kappa = 0.72
Agreement for each sub-category is also given, ranging from 0.276 to 0.879 
 
 58. __Offensive Comments in the Brazilian Web: A Dataset and Baseline Results__* Reference: de Pelle, R. and Moreira, V., 2017. Offensive Comments in the Brazilian Web: A Dataset and Baseline Results. In: VI Brazilian Workshop on Social Network Analysis and Mining. SBC. 
 * Link to publication: [http://www.each.usp.br/digiampietri/BraSNAM/2017/p04.pdf] (http://www.each.usp.br/digiampietri/BraSNAM/2017/p04.pdf)* Link to data: https://github.com/rogersdepelle/OffComBR 
 * Task description: Binary (offensive content / not)
Target of abuse is also annotated (Xenophobia, homophobia, sexism, racism, cursing, religious intolerance) 
 * Details of task: Religion/creed, Race/ethnicity, Physical/disability, Gender/sexual orientation 
 * Size of dataset: 1250 
 * Percentage abusive: 0.33 
 * Language: Portugese 
 * Level of annotation: Posts 
 * Platform: g1.globo.com 
 * Medium: Text 
 * Annotation process: Annotation process not given: whether expert or crowdsourced is not identified.
Note: comments on the website already undergo an annotation process. 
 * Annotation agreement: Kappa Fleiss: 0.71 
  
  
  ### Slovene
 59. __Datasets of Slovene and Croatian Moderated News Comments__* Reference: Ljubešić, N., Erjavec, T. and Fišer, D., 2018. Datasets of Slovene and Croatian Moderated News Comments. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.124-131. 
 * Link to publication: [https://www.aclweb.org/anthology/W18-5116] (https://www.aclweb.org/anthology/W18-5116)* Link to data: http://hdl.handle.net/11356/1201 
 * Task description: Binary (Deleted, Not) 
 * Details of task: Flagged content 
 * Size of dataset: 7600000 
 * Percentage abusive: 0.08 
 * Language: Slovene 
 * Level of annotation: Posts 
 * Platform: MMC RTV website 
 * Medium: Text 
 * Annotation process: Flagged by professional moderators 
 * Annotation agreement: N/A 
  
  
### Spanish
 60. __Overview of MEX-A3T at IberEval 2018: Authorship and Aggressiveness Analysis in Mexican Spanish Tweets__* Reference: Alvarez-Carmona, M., Guzman-Falcon, E., Montes-y-Gomez, M., Escalante, H., Villasenor-Pineda, L., Reyes-Meza, V. and Rico-Sulayes, A., 2018. Overview of MEX-A3T at IberEval 2018: Authorship and aggressiveness analysis in Mexican Spanish tweets. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 
 * Link to publication: [http://ceur-ws.org/Vol-2150/overview-mex-a3t.pdf] (http://ceur-ws.org/Vol-2150/overview-mex-a3t.pdf)* Link to data: https://mexa3t.wixsite.com/home/aggressive-detection-track 
 * Task description: Binary (aggressive / not aggressive) 
 * Details of task: Group-directed 
 * Size of dataset: 11000 
 * Percentage abusive: 0.32 
 * Language: Spanish 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Two annotators (they appear to be experts with experience in the field).
Initial, pilot labelling (to clarify the rules) and then full labelling. 
 * Annotation agreement: Kappa (pilot): 0.424
Kappa (final): 0.587 
  
 61. __Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (Spanish)__* Reference: Fersini, E., Rosso, P. and Anzovino, M., 2018. Overview of the Task on Automatic Misogyny Identification at IberEval 2018. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 
 * Link to publication: [http://ceur-ws.org/Vol-2150/overview-AMI.pdf] (http://ceur-ws.org/Vol-2150/overview-AMI.pdf)* Link to data: https://amiibereval2018.wordpress.com/important-dates/data/ 
 * Task description: Binary (misogyny / not)
5 categories of misogyny (stereotype, dominance, derailing, sexual harassment, discredit)
Target of misogyny (active [individual directed] or passive [group directed]) 
 * Details of task: Sexism 
 * Size of dataset: 4138 
 * Percentage abusive: 0.5 
 * Language: Spanish 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Crowdsourcing: CrowdFlower platform, 3 annotators per tweet. 
Gold standard, to test Crowdsource workers, created by two annotators annotating tweets & then an expert, 3rd annotator, intervening in cases of disagreement.
 
 * Annotation agreement: Not given 
  
 62. __hatEval, SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter (Spanish)__* Reference: Basile, V., Bosco, C., Fersini, E., Nozza, D., Patti, V., Pardo, F., Rosso, P. and Sanguinetti, M., 2019. SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter. In: Proceedings of the 13th International Workshop on Semantic Evaluation. Minneapolis, Minnesota: Association for Computational Linguistics, pp.54-63. 
 * Link to publication: [https://www.aclweb.org/anthology/S19-2007] (https://www.aclweb.org/anthology/S19-2007)* Link to data: competitions.codalab.org/competitions/19935
https://github.com/msang/hateval/blob/master/annotation_guidelines.md  
 * Task description: Branching structure of tasks:
Binary (Hate, Not)
Within Hate (Group, Individual)
Within Hate (Agressive, Not) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 6600 
 * Percentage abusive: 0.4 
 * Language: Spanish 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Combination of experts and crowdsourcing.
First, Crowdsourcing: Annotators were give guidelines. 3 independent judgments per tweet. Majority label adopted.
Second, Expert: 2 experts redo annotations. Majority decision taken, using the crowdsource input as a 3rd judgement.  
 * Annotation agreement: Average confidence' used (which combines both agreement and reliability of each contributor):
Spanish: 0.89, 0.47, 0.47 


### Turkish
 63. __A Corpus of Turkish Offensive Language on Social Media__* Reference: Çöltekin, C., 2020. A Corpus of Turkish Offensive Language on Social Media. In: Proceedings of the 12th International Conference on Language Resources and Evaluation. 
 * Link to publication: [https://coltekin.github.io/offensive-turkish/troff.pdf] (https://coltekin.github.io/offensive-turkish/troff.pdf)* Link to data: https://sites.google.com/site/offensevalsharedtask/home 
 * Task description: Branching structure of tasks:
Binary (Offensive, Not)
Within Offensive (Target, Not)
Within Target (Individual, Group, Other) 
 * Details of task: Group-directed + Person-directed 
 * Size of dataset: 36232 
 * Percentage abusive: 0.19 
 * Language: Turkish 
 * Level of annotation: Posts 
 * Platform: Twitter 
 * Medium: Text 
 * Annotation process: Trained; asked to annotate; contributions from those who annotated fewer than 100 docs were dropped. Very poorly-formed messages were discarded. 
 * Annotation agreement: Top level:
92.3%; Cohen kappa of 0.761

All labels:
87.8%; kappa 0.649 
  

---

# Lists of abusive keywords

1. __Hatebase__
   * "Researchers are encouraged to take advantage of Hatebase's vocabulary dataset, which is a valuable lexicon for searching other data repositories such as public forums, as well as Hatebase's sightings dataset, which is useful for trending analysis"
   * Data link: [hatebase.org/academia](https://hatebase.org/academia)

1. __Hurtlex__
   * "HurtLex is a lexicon of offensive, aggressive, and hateful words
   in over 50 languages. The words are divided into 17 categories, plus a
   macro-category indicating whether there is stereotype involved."
   * Data link: [github.com/valeriobasile/hurtlex](https://github.com/valeriobasile/hurtlex)
   * Reference: [Hurtlex: A Multilingual Lexicon of Words to Hurt](http://ceur-ws.org/Vol-2253/paper49.pdf), Proc. CLiC-it 2018

1. __Gorrell et al.__
   * Data link: [http://staffwww.dcs.shef.ac.uk/people/G.Gorrell/publications-materials/abuse-terms.txt](http://staffwww.dcs.shef.ac.uk/people/G.Gorrell/publications-materials/abuse-terms.txt)
   * Reference: [Twits, Twats and Twaddle: Trends in Online Abuse towards UK Politicians](https://gate-socmedia.group.shef.ac.uk/wp-content/uploads/2019/07/Gorrell-Greenwood.pdf), Proc. ICWSM

1. __Wiegand et al.__
   * Data link: [https://github.com/uds-lsv/lexicon-of-abusive-words](https://github.com/uds-lsv/lexicon-of-abusive-words)
   * Reference: [Inducing a Lexicon of Abusive Words – A Feature-Based Approach](https://www.aclweb.org/anthology/N18-1095.pdf), Proc. NAACL-HLT 2018

1. __Chandrasekharan et al.__
   * Data link: [Reddit hate lexicon](https://www.dropbox.com/sh/5ud4fwxvb6q7k20/AAAH_SN8i5cfmJRKJteEW2b2a?dl=0)
   * Reference: [You can't stay here: the efficacy of Reddit's 2015 ban examined through hate speech](http://comp.social.gatech.edu/papers/cscw18-chand-hate.pdf), Proc. ACL Hum-Comput Interact. 

---

This page is [http://hatespeechdata.com/](http://hatespeechdata.com/).
