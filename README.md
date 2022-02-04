# Hate Speech Dataset Catalogue
<!-- **We are working on a [ckan instance](http://ckan.hatespeechdata.com) -- please give it a look! Contributions welcome :)** -->


This page catalogues datasets annotated for hate speech, online abuse, and offensive language. They may be useful for e.g. training a natural language processing system to detect this language.

The list is maintained by [Leon Derczynski](https://www.derczynski.com/), [Bertie Vidgen](https://www.turing.ac.uk/people/researchers/bertie-vidgen), [Hannah Rose Kirk](https://www.hannahrosekirk.com/), Pica Johansson, [Yi-Ling Chung](https://yilingchung.github.io/), Mads Guldborg Kjeldgaard Kongsbak, [Laila Sprejer](https://www.turing.ac.uk/people/researchers/laila-sprejer), and Philine Zeinert.

We provide a list of [datasets](#Datasets-header) and [keywords](#Keywords-header). If you would like to contribute to our catalogue or add your dataset, please see the [instructions for contributing](#Contributing-header).

If you use these resources, please cite (and read!) our paper: [Directions in Abusive Language Training Data: Garbage In, Garbage Out](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0243300). And if you would like to find other resources for researching online hate, visit The Alan Turing Institute's [Online Hate Research Hub](https://www.turing.ac.uk/research/research-programmes/public-policy/online-hate-research-hub) or read The Alan Turing Institute's [Reading List on Online Hate and Abuse Research](https://docs.google.com/document/d/1WVkVGp29Jt6d-4fBnZ5OWVYuFn_03rzz-KBqPsu6gTM/edit?usp=sharing).

If you're looking for a good paper on online hate training datasets (beyond our paper, of course!) then have a look at ['Resources and benchmark corpora for hate speech detection: a systematic review'](https://link.springer.com/article/10.1007/s10579-020-09502-8) by Poletto et al. in *Language Resources and Evaluation*.

Please send contributions via github pull request. You can do this by visiting the [source code](https://github.com/leondz/hatespeechdata/blob/master/README.md) on github and clicking the edit icon (a pencil, above the text, on the right) - more details [below](#Contributing-header). There's a commented-out markdown template at the top of this file. Accompanying [data statements](https://www.mitpressjournals.org/doi/abs/10.1162/tacl_a_00041) preferred for all corpora.

<a id="Datasets-header"></a>
# Datasets Table of Contents

* [Arabic](#Arabic-header)
* [Bengali](#Bengali-header)
* [Croatian](#Croatian-header)
* [Danish](#Danish-header)
* [English](#English-header)
* [Estonian](#Estonian-header)
* [French](#French-header)
* [German](#German-header)
* [Greek](#Greek-header)
* [Hindi](#Hindi-header)
* [Indonesian](#Indonesian-header)
* [Latvian](#Latvian-header)
* [Portuguese](#Portuguese-header)
* [Polish](#Polish-header)
* [Russian](#Russian-header)
* [Slovene](#Slovene-header)
* [Spanish](#Spanish-header)
* [Turkish](#Turkish-header)
* [Ukranian](#Ukranian-header)


## List of datasets
<!-- dataset template

### TITLE
* Link to publication: [url](url) - link to the documentation and/or a data statement about the data
* Link to data: [url](url) - direct download is preferred, e.g. a link straight to a .zip file
* Task description: How the task is framed in this data, e.g. "Binary (Hate, Not)", "Hierarchical", "Three-class (Hate speech, Offensive language, None)"
* Details of task: Free-text description of the task this data models, e.g. "Misogyny detection on social media in Danish"
* Size of dataset: Give the number of instances of abusive/non-abusive/other items
* Percentage abusive: e.g. 1.2%
* Language: e.g. Arabic
* Level of annotation: What is an "instance", in this dataset? e.g. Posts, User, Conversation, ... 
* Platform: e.g. twitter, snapchat, ..
* Medium: text / image / audio / ...
* Reference: Give a bibliographic reference for the data (if there is one), with title, author, year, venue etc

-->

<a id="Arabic-header"></a>
### Arabic
#### Are They our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere
* Link to publication: [https://ieeexplore.ieee.org/document/8508247](https://ieeexplore.ieee.org/document/8508247)
* Link to data: [https://github.com/nuhaalbadi/Arabic_hatespeech](https://github.com/nuhaalbadi/Arabic_hatespeech)
* Task description: Binary (Hate, Not) 
* Details of task: Religious subcategories 
* Size of dataset: 6,136 
* Percentage abusive: 0.45 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Albadi, N., Kurdi, M. and Mishra, S., 2018. Are they Our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere. In: International Conference on Advances in Social Networks Analysis and Mining. Barcelona, Spain: IEEE, pp.69-76. 
 
#### Multilingual and Multi-Aspect Hate Speech Analysis (Arabic)
* Link to publication: [https://arxiv.org/abs/1908.11049](https://arxiv.org/abs/1908.11049)
* Link to data: [https://github.com/HKUST-KnowComp/MLMA_hate_speech](https://github.com/HKUST-KnowComp/MLMA_hate_speech) 
* Task description: Detailed taxonomy with cross-cutting attributes: Hostility, Directness, Target Attribute, Target Group, How annotators felt on seeing the tweet.
* Details of task: Gender, Sexual orientation, Religion, Disability 
* Size of dataset: 3,353 
* Percentage abusive: 0.64 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 
 
#### L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language
* Link to publication: [https://www.aclweb.org/anthology/W19-3512](https://www.aclweb.org/anthology/W19-3512)
* Link to data: [https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset](https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset)
* Task description: Ternary (Hate, Abusive, Normal) 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 5,846 
* Percentage abusive: 0.38 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Mulki, H., Haddad, H., Bechikh, C. and Alshabani, H., 2019. L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.111-118. 

#### Abusive Language Detection on Arabic Social Media (Twitter)
* Link to publication: [https://www.aclweb.org/anthology/W17-3008](https://www.aclweb.org/anthology/W17-3008)
* Link to data: [http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx](http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx)
* Task description: Ternary (Obscene, Offensive but not obscene, Clean) 
* Details of task: Incivility 
* Size of dataset: 1,100 
* Percentage abusive: 0.59 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Mubarak, H., Darwish, K. and Magdy, W., 2017. Abusive Language Detection on Arabic Social Media. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.52-56. 
 
#### Abusive Language Detection on Arabic Social Media (Al Jazeera)
* Link to publication: [https://www.aclweb.org/anthology/W17-3008](https://www.aclweb.org/anthology/W17-3008)
* Link to data: [http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx](http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx)
* Task description: Ternary (Obscene, Offensive but not obscene, Clean) 
* Details of task: Incivility 
* Size of dataset: 32,000 
* Percentage abusive: 0.81 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: AlJazeera 
* Medium: Text 
* Reference: Mubarak, H., Darwish, K. and Magdy, W., 2017. Abusive Language Detection on Arabic Social Media. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.52-56. 

#### Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic
* Link to publication: [https://www.sciencedirect.com/science/article/pii/S1877050918321756](https://www.sciencedirect.com/science/article/pii/S1877050918321756)
* Link to data: [https://onedrive.live.com/?authkey=!ACDXj_ZNcZPqzy0&id=6EF6951FBF8217F9!105&cid=6EF6951FBF8217F9](https://onedrive.live.com/?authkey=!ACDXj_ZNcZPqzy0&id=6EF6951FBF8217F9!105&cid=6EF6951FBF8217F9)
* Task description: Binary (Offensive, Not) 
* Details of task: Incivility 
* Size of dataset: 15,050 
* Percentage abusive: 0.39 
* Language: Arabic 
* Level of annotation: Posts 
* Platform: YouTube 
* Medium: Text 
* Reference: Alakrot, A., Murray, L. and Nikolov, N., 2018. Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic. Procedia Computer Science, 142, pp.174-181. 

<a id="Bengali-header"></a>
### Bengali
#### Hate Speech Detection in the Bengali language: A Dataset and its Baseline Evaluation
* Link to publication: [https://arxiv.org/pdf/2012.09686.pdf](https://arxiv.org/pdf/2012.09686.pdf)
* Link to data: [https://www.kaggle.com/naurosromim/bengali-hate-speech-dataset](https://www.kaggle.com/naurosromim/bengali-hate-speech-dataset)
* Task description: Binary (hateful, not)
* Details of task: Several categories: sports, entertainment, crime, religion, politics, celebrity and meme
* Size of dataset: 30,000
* Percentage abusive: 0.33
* Language: Bengali
* Level of annotation: Posts
* Platform: Youtube and Facebook
* Medium: Text 
* Reference: Romim, N., Ahmed, M., Talukder, H., & Islam, M. S. (2021). Hate speech detection in the bengali language: A dataset and its baseline evaluation. In Proceedings of International Joint Conference on Advances in Computational Intelligence (pp. 457-468). Springer, Singapore.

<a id="Croatian-header"></a>
### Croatian
#### Datasets of Slovene and Croatian Moderated News Comments
* Link to publication: [https://www.aclweb.org/anthology/W18-5116](https://www.aclweb.org/anthology/W18-5116)
* Link to data: [http://hdl.handle.net/11356/1202](http://hdl.handle.net/11356/1202)
* Task description: Binary (Deleted, Not) 
* Details of task: Flagged content 
* Size of dataset: 17,000,000 
* Percentage abusive: 0.02 
* Language: Croatian 
* Level of annotation: Posts 
* Platform: 24sata website 
* Medium: Text 
* Reference: Ljubešić, N., Erjavec, T. and Fišer, D., 2018. Datasets of Slovene and Croatian Moderated News Comments. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.124-131. 

#### Automating News Comment Moderation with Limited Resources: Benchmarking in Croatian and Estonian
* Link to publication: [https://jlcl.org/content/2-allissues/1-heft1-2020/jlcl_2020-1_3.pdf](https://jlcl.org/content/2-allissues/1-heft1-2020/jlcl_2020-1_3.pdf)
* Link to data: [https://www.clarin.si/repository/xmlui/handle/11356/1399](https://www.clarin.si/repository/xmlui/handle/11356/1399)
* Task description: Multi-class based on Different rules 
* Details of task: Flagged content performmed by the real newspaper moderators
* Size of dataset: 21M 
* Percentage abusive: 7.8% 
* Language: Croatian 
* Level of annotation: Posts 
* Platform: Newspaper comments  
* Medium: Text 
* Reference: Ravi Shekhar, Marko Pranjić, Senja Pollak, Andraž Pelicon, Matthew Purver (2020). Automating News Comment Moderation with Limited Resources: Benchmarking in Croatian and Estonian. Journal for Language Technology and Computational Linguistics (JLCL). 

<a id="Danish-header"></a>
### Danish
#### Offensive Language and Hate Speech Detection for Danish
* Link to publication: [http://www.derczynski.com/papers/danish_hsd.pdf](http://www.derczynski.com/papers/danish_hsd.pdf)
* Link to data: [https://figshare.com/articles/Danish_Hate_Speech_Abusive_Language_data/12220805](https://sites.google.com/site/offensevalsharedtask/home)
* Task description: Branching structure of tasks: Binary (Offensive, Not), Within Offensive (Target, Not), Within Target (Individual, Group, Other) 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 3,600 
* Percentage abusive: 0.12 
* Language: Danish 
* Level of annotation: Posts 
* Platform: Twitter, Reddit, newspaper comments 
* Medium: Text 
* Reference: Sigurbergsson, G. and Derczynski, L., 2019. Offensive Language and Hate Speech Detection for Danish. ArXiv. 

#### BAJER: Misogyny in Danish
* Link to publication: [https://aclanthology.org/2021.acl-long.247/](https://aclanthology.org/2021.acl-long.247/)
* Link to data: [request here](https://docs.google.com/forms/d/e/1FAIpQLSfUKb7ZTKd01syaNkAW5GDfCSkaVsJlom06g_mJdWUkUikVHA/viewform)
* Task description: Hierarchy of abusive content labels including subcategories of misogyny
* Details of task: "Misogyny detection on social media in Danish"
* Size of dataset: 27.9K comments
* Percentage abusive: 7% misogynistic, 27% abusive (i.e. 20% abusive but not misogyny)
* Language: Danish
* Level of annotation: Social media post / comment
* Platform: Twitter, Facebook, Reddit
* Medium: text
* Reference: Zeinert, Inie, & Derczynski, 2021. "Annotating Online Misogyny". Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing, ACL

<a id="English-header"></a>
### English

#### The 'Call me sexist, but' sexism dataset
* Link to publication: [https://ojs.aaai.org/index.php/ICWSM/article/view/18085/17888](https://ojs.aaai.org/index.php/ICWSM/article/view/18085/17888)
* Link to data: [https://doi.org/10.7802/2251](https://doi.org/10.7802/2251) 
* Task description: Sexism detection based on content and phrasing
* Details of task: Sexism detection on English social media data informed by survey items measuring sexist attitudes and adversarial examples
* Size of dataset: 6325
* Percentage abusive: 28%
* Language: English
* Level of annotation: tweets and survey items
* Platform: Twitter, Social Psychology scales
* Medium: text
* Reference: Samory, M., Sen, I., Kohne, J., Flöck, F. and Wagner, C., 2021, May. Call me sexist, but…: Revisiting sexism detection using psychological scales and adversarial samples. In Intl AAAI Conf. Web and Social Media (pp. 573-584).

#### Do You Really Want to Hurt Me? Predicting Abusive Swearing in Social Media
* Link to publication: [https://www.aclweb.org/anthology/2020.lrec-1.765.pdf](https://www.aclweb.org/anthology/2020.lrec-1.765.pdf)
* Link to data: [https://github.com/dadangewp/SWAD-Repository](https://github.com/dadangewp/SWAD-Repository)
* Task description: Binary (abusive swear word, non-abusive swear word)
* Details of task: Abusive swearing
* Size of dataset: 1,511 swear words (1675 tweets)
* Percentage abusive: 0.41% (word level), 0.51% (post level)
* Language: English 
* Level of annotation: Words
* Platform: Twitter
* Medium: Text 
* Reference: Pamungkas, E. W., Basile, V., & Patti, V. (2020). Do you really want to hurt me? predicting abusive swearing in social media. In The 12th Language Resources and Evaluation Conference (pp. 6237-6246). European Language Resources Association.

#### Multimodal Meme Dataset (MultiOFF) for Identifying Offensive Content in Image and Text
* Link to publication: [https://www.aclweb.org/anthology/2020.trac-1.6.pdf](https://www.aclweb.org/anthology/2020.trac-1.6.pdf)
* Link to data: [https://github.com/bharathichezhiyan/Multimodal-Meme-Classification-Identifying-Offensive-Content-in-Image-and-Text](https://github.com/bharathichezhiyan/Multimodal-Meme-Classification-Identifying-Offensive-Content-in-Image-and-Text)
* Task description: Binary (offensive, non-offensive)
* Details of task: Hate per se (related to 2016 U.S. presidential election)
* Size of dataset: 743
* Percentage abusive: 0.41%
* Language: English 
* Level of annotation: Posts
* Platform: Kaggle, Reddit, Facebook, Twitter and Instagram
* Medium: Text and Images/memes
* Reference: Suryawanshi, S., Chakravarthi, B. R., Arcan, M., & Buitelaar, P. (2020, May). Multimodal meme dataset (MultiOFF) for identifying offensive content in image and text. In Proceedings of the Second Workshop on Trolling, Aggression and Cyberbullying (pp. 32-41).

#### Hatemoji: A Test Suite and Adversarially-Generated Dataset for Benchmarking and Detecting Emoji-based Hate
* Link to publication: [https://arxiv.org/abs/2108.05921](https://arxiv.org/abs/2108.05921)
* Link to data: [https://github.com/HannahKirk/Hatemoji](https://github.com/HannahKirk/Hatemoji)
* Task description: Branching structure of tasks: Binary (Hate, Not Hate), Within Hate (Type, Target)
* Details of task: Hate speech detection for text statements including emoji, consisting of a checklist-based test suite (HatemojiCheck) and an adversarially-generated dataset (HatemojiBuild)
* Size of dataset: HatemojiCheck = 3,930; HatemojiBuild = 5,912.
* Percentage abusive: HatemojiCheck = 69%, HatemojiBuild = 50%
* Language: English
* Level of annotation: Post
* Platform: Synthetically-Generated
* Medium: Text with emoji
* Reference: Kirk, H. R., Vidgen, B., Röttger, P., Thrush, T., & Hale, S. A. 2021. Hatemoji: A test suite and adversarially-generated dataset for benchmarking and detecting emoji-based hate. arXiv preprint arXiv:2108.05921.

#### Semeval-2021 Task 5: Toxic Spans Detection
* Link to publication: [https://aclanthology.org/2021.semeval-1.6.pdf](https://aclanthology.org/2021.semeval-1.6.pdf)
* Link to data: [https://github.com/ipavlopoulos/toxic_spans](https://github.com/ipavlopoulos/toxic_spans)
* Task description: Binary toxic spans (toxic, non-toxic)
* Details of task: Hate per se
* Size of dataset: 10,629
* Percentage abusive: 0.56
* Language: English 
* Level of annotation: Phrases
* Platform: Civil Comments
* Medium: Text 
* Reference: Pavlopoulos, J., Sorensen, J., Laugier, L., & Androutsopoulos, I. (2021, August). Semeval-2021 task 5: Toxic spans detection. In Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021) (pp. 59-69).

#### Human-in-the-Loop for Data Collection: a Multi-Target Counter Narrative Dataset to Fight Online Hate Speech
* Link to publication: [https://aclanthology.org/2021.acl-long.250.pdf](https://aclanthology.org/2021.acl-long.250.pdf)
* Link to data: [https://github.com/marcoguerini/CONAN](https://github.com/marcoguerini/CONAN)
* Task description: Binary (hateful, not)
* Details of task: race, religion, country of origin, sexual orientation, disability, gender
* Size of dataset: 5,003
* Percentage abusive: 1
* Language: English 
* Level of annotation: Posts
* Platform: Semi-synthetic text
* Medium: Text 
* Reference: Margherita Fanton, Helena Bonaldi, Serra Sinem Tekiroğlu, Marco Guerini Human-in-the-Loop for Data Collection: a Multi-Target Counter Narrative Dataset to Fight Online Hate Speech In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics: Long Papers.

#### HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection
* Link to publication: [https://arxiv.org/abs/2012.10289](https://arxiv.org/abs/2012.10289)
* Link to data: [https://github.com/punyajoy/HateXplain](https://github.com/punyajoy/HateXplain)
* Task description: Level of hate (hate, offensive or normal), on target groups (race, religion, gender, sexual orientation, miscellaneous), and rationales
* Details of task: Hate per se
* Size of dataset: 20,148
* Percentage abusive: 0.57
* Language: English 
* Level of annotation: Words, phrases, posts
* Platform: Twitter and Gab
* Medium: Text 
* Reference: Mathew, B., Saha, P., Yimam, S. M., Biemann, C., Goyal, P., & Mukherjee, A. (2021, May). HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 35, No. 17, pp. 14867-14875).

#### ALONE: A Dataset for Toxic Behavior among Adolescents on Twitter
* Link to publication: [https://arxiv.org/pdf/2008.06465.pdf](https://arxiv.org/pdf/2008.06465.pdf)
* Link to data: Data made available upon request, please email Ugur Kursuncu ugur@gsu.edu and thilini@sc.edu thilini@sc.edu.
* Task description: Binary (Toxic, Non-Toxic) 
* Details of task: Annotates interactions (Tweets and their replies), and assigns keywords describing use of emojis, URL content and images.   
* Size of dataset: 688
* Percentage abusive: 0.17
* Language: English 
* Level of annotation: Post
* Platform: Twitter
* Medium: Multimodal (text, images, emojis, metadata)
* Reference: Wijesiriwardene, T., Inan, H., Kursuncu, U., Gaur, M., Shalin, V., Thirunarayan, K., Sheth, A. and Arpinar, I., 2020, Arxiv. 

#### Towards a Comprehensive Taxonomy and Large-Scale Annotated Corpus for Online Slur Usage
* Link to publication: [https://www.aclweb.org/anthology/2020.alw-1.17.pdf](https://www.aclweb.org/anthology/2020.alw-1.17.pdf)
* Link to data: [https://github.com/networkdynamics/slur-corpus](https://github.com/networkdynamics/slur-corpus)
* Task description: 4 primary categories (derogatory, appropriate, non-derogatory/non-appropriate, homonyms, noise)
* Details of task: Hate per se
* Size of dataset: 39,811
* Percentage abusive: 0.52
* Language: English 
* Level of annotation: Posts
* Platform: Reddit
* Medium: Text 
* Reference: Kurrek, J., Saleem, H. M., & Ruths, D. (2020, November). Towards a comprehensive taxonomy and large-scale annotated corpus for online slur usage. In Proceedings of the Fourth Workshop on Online Abuse and Harms (pp. 138-149).

#### Multimodal Meme Dataset (MultiOFF) for Identifying Offensive Content in Image and Text
* Link to publication: [https://www.aclweb.org/anthology/2020.trac-1.6.pdf](https://www.aclweb.org/anthology/2020.trac-1.6.pdf)
* Link to data: [https://www.aclweb.org/anthology/2020.trac-1.6.pdf](https://www.aclweb.org/anthology/2020.trac-1.6.pdf)
* Task description: Binary (offensive, non-offensive)
* Details of task: Hate per se (related to 2016 U.S. presidential election)
* Size of dataset: 743
* Percentage abusive: 0.41
* Language: English 
* Level of annotation: Posts
* Platform: Kaggle, Reddit, Facebook, Twitter and Instagram
* Medium: Text and Images/memes
* Reference: Suryawanshi, S., Chakravarthi, B. R., Arcan, M., & Buitelaar, P. (2020, May). Multimodal meme dataset (MultiOFF) for identifying offensive content in image and text. In Proceedings of the Second Workshop on Trolling, Aggression and Cyberbullying (pp. 32-41).

#### Predicting the Type and Target of Offensive Posts in Social Media
* Link to publication: [https://aclanthology.org/N19-1144.pdf](https://aclanthology.org/N19-1144.pdf)
* Link to data: [https://scholar.harvard.edu/malmasi/olid](https://scholar.harvard.edu/malmasi/olid)
* Task description: Branching structure of tasks. A: offensive / not, B: targeted insult / untargeted, C: individual, group, other.
* Details of task: Hate per se
* Size of dataset: 14,100
* Percentage abusive: 0.33
* Language: English 
* Level of annotation: Posts
* Platform: Twitter
* Medium: Text 
* Reference: Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N., & Kumar, R. (2019, June). Predicting the Type and Target of Offensive Posts in Social Media. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) (pp. 1415-1420).

#### Nuanced metrics for measuring unintended bias with real data for text classification
* Link to publication: [https://arxiv.org/pdf/1903.04561.pdf](https://arxiv.org/pdf/1903.04561.pdf)
* Link to data: [https://www.tensorflow.org/datasets/catalog/civil_comments](https://www.tensorflow.org/datasets/catalog/civil_comments)
* Task description: Toxicity (severe, obscene, threat, insult, identity attack, sexual explicit), and several identity attributes (e.g., gender, religion and race)
* Details of task: Hate per se
* Size of dataset: 1,804,875
* Percentage abusive: 0.8
* Language: English 
* Level of annotation: Comments/posts
* Platform: Civil Comments
* Medium: Text 
* Reference: Borkan, D., Dixon, L., Sorensen, J., Thain, N., & Vasserman, L. (2019, May). Nuanced metrics for measuring unintended bias with real data for text classification. In Companion proceedings of the 2019 world wide web conference (pp. 491-500).

#### Introducing CAD: the Contextual Abuse Dataset
* Link to publication: [https://aclanthology.org/2021.naacl-main.182.pdf](https://aclanthology.org/2021.naacl-main.182.pdf)
* Link to data: [https://zenodo.org/record/4881008#.Ye6OwhP7R6o](https://zenodo.org/record/4881008#.Ye6OwhP7R6o)
* Task description: Contextually abusive language, person-directed + group-directed 
* Details of task: Primary categories (secondary categories): Abusive + Identity-directed (derogation/animosity/threatening/glorification/dehumanization), Abusive + Person-directed (derogation/animosity/threatening/glorification/dehumanization), Abusive + Affiliation directed (abuse to them/abuse about them), Counter Speech (against identity-directed abuse/against affiliation-directed abuse/against person-directed abuse), Non-hateful Slurs and Neutral.
* Size of dataset: 25,000
* Percentage abusive: Affiliation-directed, 6%; Identity-directed, 13%; Person-directed, 5%
* Language: English
* Level of annotation: Conversation thread 
* Platform: Reddit 
* Medium: Text
* Reference: Vidgen, B., Nguyen, D., Margetts, H., Rossini, P., and Troble, R., Introducing CAD: the Contextual Abuse Dataset, 2021, In: Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp.2289–2303

#### Automated Hate Speech Detection and the Problem of Offensive Language
* Link to publication: [https://arxiv.org/pdf/1703.04009.pdf](https://arxiv.org/pdf/1703.04009.pdf)
* Link to data: [https://github.com/t-davidson/hate-speech-and-offensive-language](https://github.com/t-davidson/hate-speech-and-offensive-language)
* Task description: Hierarchy (Hate, Offensive, Neither) 
* Details of task: Hate per se 
* Size of dataset: 24,802 
* Percentage abusive: 0.06 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Davidson, T., Warmsley, D., Macy, M. and Weber, I., 2017. Automated Hate Speech Detection and the Problem of Offensive Language. ArXiv,. 

#### Hate Speech Dataset from a White Supremacy Forum
* Link to publication: [https://www.aclweb.org/anthology/W18-5102.pdf](https://www.aclweb.org/anthology/W18-5102.pdf)
* Link to data: [https://github.com/Vicomtech/hate-speech-dataset](https://github.com/Vicomtech/hate-speech-dataset)
* Task description: Ternary (Hate, Relation, Not)
* Details of task: Hate per se 
* Size of dataset: 9,916 
* Percentage abusive: 0.11 
* Language: English 
* Level of annotation: Sentence - with context of the converstaional thread taken into account 
* Platform: Stormfront 
* Medium: Text 
* Reference: de Gibert, O., Perez, N., García-Pablos, A., and Cuadros, M., 2018. Hate Speech Dataset from a White Supremacy Forum. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.11-20. 
  
#### Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter
* Link to publication: [https://www.aclweb.org/anthology/N16-2013](https://www.aclweb.org/anthology/N16-2013)
* Link to data: [https://github.com/ZeerakW/hatespeech](https://github.com/ZeerakW/hatespeech)
* Task description: 3-topic (Sexist, Racist, Not) 
* Details of task: Racism, Sexism 
* Size of dataset: 16,914 
* Percentage abusive: 0.32 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Waseem, Z. and Horvy, D., 2016. Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter. In: Proceedings of the NAACL Student Research Workshop. San Diego, California: Association for Computational Linguistics, pp.88-93. 

#### Detecting Online Hate Speech Using Context Aware Models
* Link to publication: [https://arxiv.org/pdf/1710.07395.pdf](https://arxiv.org/pdf/1710.07395.pdf)
* Link to data: [https://github.com/sjtuprog/fox-news-comments](https://github.com/sjtuprog/fox-news-comments) 
* Task description: Binary (Hate / not)
* Details of task: Hate per se 
* Size of dataset: 1528 
* Percentage abusive: 0.28 
* Language: English 
* Level of annotation: Posts 
* Platform: Fox News 
* Medium: Text 
* Reference: Gao, L. and Huang, R., 2018. Detecting Online Hate Speech Using Context Aware Models. ArXiv,. 

### The Gab Hate Corpus: A collection of 27k posts annotated for hate speech
* Link to publication: [https://psyarxiv.com/hqjxn/](https://psyarxiv.com/hqjxn/)
* Link to data: [https://osf.io/edua3/](https://osf.io/edua3/)
* Task description: Binary (Hate vs. Offensive/Vulgarity), Binary (Assault on human Dignity/Call for Violence – sub task on message delivery, binary: explicit/implicit), Multinomial classification: Identity based hate (race/ethnicity, nationality/regionalism/xenophobia, gender, religion/belief system, sexual orientation, ideology, political identification/party, mental/physical health)  
* Details of task: Group-directed + Person-directed
* Size of dataset: 27,665 
* Percentage abusive: 0.09 Hate, 0.06 Offensive/Vulgar
* Language: English
* Level of annotation: Post
* Platform: Gab
* Medium: Text
* Reference: Kennedy, B., Araria, M., Mostafazadeh Davani, A., Yeh, L., Omrani, A., Kim, Y., Koombs, K., Havaldar, S., Portillo-Wightman, G., Gonzalez, E., Hoover, J., Azatain, A., Hussain, A., Lara, A., Olmos, G., Omary, A., Park, C., Wang, C., Wang, X., Zhang, Y. and Dehghani, M., 2018, The Gab Hate Corpus: A collection of 27k posts annotated for hate speech. PsyArXiv. 
 
#### Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter
* Link to publication: [https://pdfs.semanticscholar.org/3eeb/b7907a9b94f8d65f969f63b76ff5f643f6d3.pdf](https://pdfs.semanticscholar.org/3eeb/b7907a9b94f8d65f969f63b76ff5f643f6d3.pdf)
* Link to data: [https://github.com/ZeerakW/hatespeech](https://github.com/ZeerakW/hatespeech)
* Task description: Multi-topic (Sexist, Racist, Neither, Both) 
* Details of task: Racism, Sexism 
* Size of dataset: 4,033 
* Percentage abusive: 0.16 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Waseem, Z., 2016. Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter. In: Proceedings of 2016 EMNLP Workshop on Natural Language Processing and Computational Social Science. Copenhagen, Denmark: Association for Computational Linguistics, pp.138-142. 

#### When Does a Compliment Become Sexist? Analysis and Classification of Ambivalent Sexism Using Twitter Data
* Link to publication: [https://pdfs.semanticscholar.org/225f/f8a6a562bbb64b22cebfcd3288c6b930d1ef.pdf](https://pdfs.semanticscholar.org/225f/f8a6a562bbb64b22cebfcd3288c6b930d1ef.pdf)
* Link to data: [https://github.com/AkshitaJha/NLP_CSS_2017](https://github.com/AkshitaJha/NLP_CSS_2017)
* Task description: Hierarchy of Sexism (Benevolent sexism, Hostile sexism, None) 
* Details of task: Sexism 
* Size of dataset: 712 
* Percentage abusive: 1 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Jha, A. and Mamidi, R., 2017. When does a Compliment become Sexist? Analysis and Classification of Ambivalent Sexism using Twitter Data. In: Proceedings of the Second Workshop on Natural Language Processing and Computational Social Science. Vancouver, Canada: Association for Computational Linguistics, pp.7-16. 

#### Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (English)
* Link to publication: [http://ceur-ws.org/Vol-2150/overview-AMI.pdf](http://ceur-ws.org/Vol-2150/overview-AMI.pdf)
* Link to data: [https://amiibereval2018.wordpress.com/im
nt-dates/data/](https://amiibereval2018.wordpress.com/important-dates/data/)
* Task description: Binary (misogyny / not), 5 categories (stereotype, dominance, derailing, sexual harassment, discredit), target of misogyny (active or passive)
* Details of task: Sexism 
* Size of dataset: 3,977 
* Percentage abusive: 0.47 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Fersini, E., Rosso, P. and Anzovino, M., 2018. Overview of the Task on Automatic Misogyny Identification at IberEval 2018. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 
 
#### CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English)
* Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf](https://www.aclweb.org/anthology/P19-1271.pdf)
* Link to data: [https://github.com/marcoguerini/CONAN](https://github.com/marcoguerini/CONAN)
* Task description: Binary (Islamophobic / not), multi-topic (Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic)
* Details of task: Islamophobia 
* Size of dataset: 1,288 
* Percentage abusive: 1 
* Language: English 
* Level of annotation: Posts 
* Platform: Synthetic / Facebook 
* Medium: Text 
* Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 


#### Characterizing and Detecting Hateful Users on Twitter
* Link to publication: [https://arxiv.org/pdf/1803.08977.pdf](https://arxiv.org/pdf/1803.08977.pdf)
* Link to data: [https://github.com/manoelhortaribeiro/HatefulUsersTwitter](https://github.com/manoelhortaribeiro/HatefulUsersTwitter)
* Task description: Binary (hateful/not)
* Details of task: Hate per se 
* Size of dataset: 4,972 
* Percentage abusive: 0.11 
* Language: English 
* Level of annotation: Users 
* Platform: Twitter 
* Medium: Text 
* Reference: Ribeiro, M., Calais, P., Santos, Y., Almeida, V. and Meira, W., 2018. Characterizing and Detecting Hateful Users on Twitter. ArXiv,. 


#### A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Gab)
* Link to publication: [https://arxiv.org/abs/1909.04251](https://arxiv.org/abs/1909.04251)
* Link to data: [https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech)
* Task description: Binary (hateful/not) 
* Details of task: Hate per se 
* Size of dataset: 33,776 
* Percentage abusive: 0.43 
* Language: English 
* Level of annotation: Posts (in the context of a conversation) 
* Platform: Gab 
* Medium: Text 
* Reference: Qian, J., Bethke, A., Belding, E. and Yang Wang, W., 2019. A Benchmark Dataset for Learning to Intervene in Online Hate Speech. ArXiv,. 

#### A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Reddit)
* Link to publication: [https://arxiv.org/abs/1909.04251](https://arxiv.org/abs/1909.04251)
* Link to data: [https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech)
* Task description: Binary (hateful/not)
* Details of task: Hate per se 
* Size of dataset: 22,324 
* Percentage abusive: 0.24 
* Language: English 
* Level of annotation: Posts (with context of the converstaional thread taken into account)
* Platform: Reddit 
* Medium: Text 
* Reference: Qian, J., Bethke, A., Belding, E. and Yang Wang, W., 2019. A Benchmark Dataset for Learning to Intervene in Online Hate Speech. ArXiv,. 

#### Multilingual and Multi-Aspect Hate Speech Analysis (English)
* Link to publication: [https://arxiv.org/abs/1908.11049](https://arxiv.org/abs/1908.11049)
* Link to data: [https://github.com/HKUST-KnowComp/MLMA_hate_speech](https://github.com/HKUST-KnowComp/MLMA_hate_speech)
* Task description: Detailed taxonomy with cross-cutting attributes: Hostility, Directness, Target attribute and Target group.
* Details of task: Gender, Sexual orientation, Religion, Disability 
* Size of dataset: 5,647 
* Percentage abusive: 0.76 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 
  
  
#### Exploring Hate Speech Detection in Multimodal Publications
* Link to publication: [https://arxiv.org/pdf/1910.03814.pdf](https://arxiv.org/pdf/1910.03814.pdf)
* Link to data: [https://gombru.github.io/2019/10/09/MMHS/](https://gombru.github.io/2019/10/09/MMHS/)
* Task description: Six primary categories (No attacks to any community, Racist, Sexist, Homophobic, Religion based attack, Attack to other community)
* Details of task: Racism, Sexism, Homophobia, Religion-based attack 
* Size of dataset: 149,823 
* Percentage abusive: 0.25 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text and Images/Memes 
* Reference: Gomez, R., Gibert, J., Gomez, L. and Karatzas, D., 2019. Exploring Hate Speech Detection in Multimodal Publications. ArXiv,. 
  
#### Predicting the Type and Target of Offensive Posts in Social Media
* Link to publication: [https://arxiv.org/pdf/1902.09666.pdf](https://arxiv.org/pdf/1902.09666.pdf)
* Link to data: [http://competitions.codalab.org/ competitions/20011](http://competitions.codalab.org/ competitions/20011)
* Task description: Branching structure of tasks: Binary (Offensive, Not), Within Offensive (Target, Not), Within Target (Individual, Group, Other) 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 14,100 
* Percentage abusive: 0.33 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N. and Kumar, R., 2019. SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval). ArXiv,. 


#### hatEval, SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter (English)
* Link to publication: [https://www.aclweb.org/anthology/S19-2007](https://www.aclweb.org/anthology/S19-2007)
* Link to data: [http://competitions.codalab.org/competitions/19935](competitions.codalab.org/competitions/19935)
* Task description: Branching structure of tasks: Binary (Hate, Not), Within Hate (Group, Individual), Within Hate (Agressive, Not)
* Details of task: Group-directed + Person-directed 
* Size of dataset: 13,000 
* Percentage abusive: 0.4 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Basile, V., Bosco, C., Fersini, E., Nozza, D., Patti, V., Pardo, F., Rosso, P. and Sanguinetti, M., 2019. SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter. In: Proceedings of the 13th International Workshop on Semantic Evaluation. Minneapolis, Minnesota: Association for Computational Linguistics, pp.54-63.

#### Peer to Peer Hate: Hate Speech Instigators and Their Targets
* Link to publication: [https://aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/view/17905/16996](https://aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/view/17905/16996)
* Link to data: [https://github.com/mayelsherif/hate_speech_icwsm18](https://github.com/mayelsherif/hate_speech_icwsm18)
* Task description: Binary (Hate/Not), only for tweets which have both a Hate Instigator and Hate Target
* Details of task: Hate per se 
* Size of dataset: 27,330 
* Percentage abusive: 0.98 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: ElSherief, M., Nilizadeh, S., Nguyen, D., Vigna, G. and Belding, E., 2018. Peer to Peer Hate: Hate Speech Instigators and Their Targets. In: Proceedings of the Twelfth International AAAI Conference on Web and Social Media (ICWSM 2018). Santa Barbara, California: University of California, pp.52-61. 
  
#### Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages
* Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true](https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)
* Link to data: [https://hasocfire.github.io/hasoc/2019/dataset.html](https://hasocfire.github.io/hasoc/2019/dataset.html) 
* Task description: Branching structure of tasks. A: Hate / Offensive or Neither, B: Hatespeech, Offensive, or Profane, C: Targeted or Untargeted 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 7,005 
* Percentage abusive: 0.36 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter and Facebook 
* Medium: Text 
* Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 

#### Detecting East Asian Prejudice on Social media
* Link to publication: [https://www.aclweb.org/anthology/2020.alw-1.19.pdf](https://www.aclweb.org/anthology/2020.alw-1.19.pdf)
* Link to data: [https://zenodo.org/record/3816667](https://zenodo.org/record/3816667)
* Task description: Task 1: Thematic annotation (East Asia/Covid-19) Task 2: Primary category annotation: 1) Hostility against an East Asian (EA) entity 2) Criticism of an East Asian entity 3) Counter speech 5) Discussion of East Asian prejudice 5) Non-related. Task 3: Secondary category annotation (if (1) or (2) - identifying what East Asian entity was targeted + if (1) interpersonal abuse/threatening language/dehumanization). 
* Details of task: Detecting East Asian prejudice 
* Size of dataset: 20,000
* Percentage abusive: 27% (Hostility, 19.5%; Criticism, 7.2%)
* Language: English 
* Level of annotation: Post
* Platform: Twitter
* Medium: Text
* Reference: Vidgen, B., Botelho, A., Broniatowski, D., Guest, E., Hall, M., Margetts, H., Tromble, R., Waseem, Z. and Hale, S., Detecting East Asian Prejudice on Social media, 2020, In: Proceedings of the Fourth Workshop on Online Abuse and Harms, pp.162–172 

#### Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior
* Link to publication: [https://arxiv.org/pdf/1802.00393.pdf](https://arxiv.org/pdf/1802.00393.pdf)
* Link to data: [https://dataverse.mpi-sws.org/dataset.xhtml?persistentId=doi:10.5072/FK2/ZDTEMN](https://dataverse.mpi-sws.org/dataset.xhtml?persistentId=doi:10.5072/FK2/ZDTEMN)
* Task description: Multi-thematic (Abusive, Hateful, Normal, Spam) 
* Details of task: Hate per se 
* Size of dataset: 80,000 
* Percentage abusive: 0.18 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Annotation process: Very detailed information is given: multiple rounds, using a smaller 300 tweet dataset for testing the schema. For the final 80k, 5 judgements per tweet. CrowdFlower 
* Annotation agreement: 55.9% = 4/5, 36.6% = 3/5, 7.5% = 2/5 
* Reference: Founta, A., Djouvas, C., Chatzakou, D., Leontiadis, I., Blackburn, J., Stringhini, G., Vakali, A., Sirivianos, M. and Kourtellis, N., 2018. Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior. ArXiv,. 

#### A Large Labeled Corpus for Online Harassment Research
* Link to publication: [http://www.cs.umd.edu/~golbeck/papers/trolling.pdf](http://www.cs.umd.edu/~golbeck/papers/trolling.pdf)
* Link to data: jgolbeck@umd.edu
* Task description: Binary (Harassment, Not) 
* Details of task: Person-directed 
* Size of dataset: 35,000 
* Percentage abusive: 0.16 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Golbeck, J., Ashktorab, Z., Banjo, R., Berlinger, A., Bhagwan, S., Buntain, C., Cheakalos, P., Geller, A., Gergory, Q., Gnanasekaran, R., Gnanasekaran, R., Hoffman, K., Hottle, J., Jienjitlert, V., Khare, S., Lau, R., Martindale, M., Naik, S., Nixon, H., Ramachandran, P., Rogers, K., Rogers, L., Sarin, M., Shahane, G., Thanki, J., Vengataraman, P., Wan, Z. and Wu, D., 2017. A Large Labeled Corpus for Online Harassment Research. In: Proceedings of the 2017 ACM on Web Science Conference. New York: Association for Computing Machinery, pp.229-233. 

#### Ex Machina: Personal Attacks Seen at Scale, Personal attacks
* Link to publication: [https://arxiv.org/pdf/1610.08914](https://arxiv.org/pdf/1610.08914)
* Link to data: [https://github.com/ewulczyn/wiki-detox](https://github.com/ewulczyn/wiki-detox)
* Task description: Binary (Personal attack, Not) 
* Details of task: Person-directed 
* Size of dataset: 115,737 
* Percentage abusive: 0.12 
* Language: English 
* Level of annotation: Posts 
* Platform: Wikipedia 
* Medium: Text 
* Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 

#### Ex Machina: Personal Attacks Seen at Scale, Toxicity
* Link to publication: [https://arxiv.org/pdf/1610.08914](https://arxiv.org/pdf/1610.08914)
* Link to data: [https://github.com/ewulczyn/wiki-detox](https://github.com/ewulczyn/wiki-detox)
* Task description: Toxicity/healthiness judgement (-2 == very toxic, 0 == neutral, 2 == very healthy) 
* Details of task: Person-directed 
* Size of dataset: 100,000 
* Percentage abusive: NA 
* Language: English 
* Level of annotation: Posts 
* Platform: Wikipedia 
* Medium: Text 
* Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 
 
#### Detecting cyberbullying in online communities (World of Warcraft)
* Link to publication: [http://aisel.aisnet.org/ecis2016_rp/61/](http://aisel.aisnet.org/ecis2016_rp/61/)
* Link to data: [http://ub-web.de/research/](http://ub-web.de/research/)
* Task description: Binary (Harassment, Not) 
* Details of task: Person-directed 
* Size of dataset: 16,975 
* Percentage abusive: 0.01 
* Language: English 
* Level of annotation: Posts 
* Platform: World of Warcraft 
* Medium: Text 
* Reference: Bretschneider, U. and Peters, R., 2016. Detecting Cyberbullying in Online Communities. Research Papers, 61. 

#### Detecting cyberbullying in online communities (League of Legends)
* Link to publication: [http://aisel.aisnet.org/ecis2016_rp/61/](http://aisel.aisnet.org/ecis2016_rp/61/)
* Link to data: [http://ub-web.de/research/](http://ub-web.de/research/)
* Task description: Binary (Harassment, Not) 
* Details of task: Person-directed 
* Size of dataset: 17,354 
* Percentage abusive: 0.01 
* Language: English 
* Level of annotation: Posts 
* Platform: League of Legends 
* Medium: Text 
* Reference: Bretschneider, U. and Peters, R., 2016. Detecting Cyberbullying in Online Communities. Research Papers, 61. 
  
#### A Quality Type-aware Annotated Corpus and Lexicon for Harassment Research
* Link to publication: [https://arxiv.org/pdf/1802.09416.pdf](https://arxiv.org/pdf/1802.09416.pdf)
* Link to data: [https://github.com/Mrezvan94/Harassment-Corpus](https://github.com/Mrezvan94/Harassment-Corpus)
* Task description: Multi-topic harassment detection
* Details of task: Racism, Sexism, Appearance-related, Intellectual, Political 
* Size of dataset: 24,189 
* Percentage abusive: 0.13 
* Language: English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Rezvan, M., Shekarpour, S., Balasuriya, L., Thirunarayan, K., Shalin, V. and Sheth, A., 2018. A Quality Type-aware Annotated Corpus and Lexicon for Harassment Research. ArXiv,.

#### Ex Machina: Personal Attacks Seen at Scale, Aggression and Friendliness
* Link to publication: [https://arxiv.org/pdf/1610.08914](https://arxiv.org/pdf/1610.08914)
* Link to data: [https://github.com/ewulczyn/wiki-detox](https://github.com/ewulczyn/wiki-detox)
* Task description: Aggression/friendliness judgement on a 5 point scale. (-2 == very aggressive, 0 == neutral, 3 == very friendly).
* Details of task: Person-Directed + Group-Directed 
* Size of dataset: 160,000 
* Percentage abusive: NA 
* Language: English 
* Level of annotation: Posts 
* Platform: Wikipedia 
* Medium: Text 
* Reference: Wulczyn, E., Thain, N. and Dixon, L., 2017. Ex Machina: Personal Attacks Seen at Scale. ArXiv,. 

#### Are Chess Discussions Racist? An Adversarial Hate Speech Data Set
* Link to publication: [https://arxiv.org/pdf/2011.10280.pdf](https://arxiv.org/pdf/2011.10280.pdf)
* Link to data: [https://www.cs.cmu.edu/~akhudabu/Chess.html](https://www.cs.cmu.edu/~akhudabu/Chess.html)
* Task description: Not Labeled
* Details of task: Racism, Misclassification
* Size of dataset: 1,000
* Percentage abusive: 0.0
* Language: English
* Level of annotation: Posts 
* Platform: Youtube
* Medium: Text 
* Reference: Rupak Sarkar and Ashiqur R. KhudaBukhsh, Nov. 2020. Are Chess Discussions Racist? An Adversarial Hate Speech Data Set. In: The Thirty-Fifth {AAAI} Conference on Artificial Intelligence, {AAAI} 2021

#### ETHOS: an Online Hate Speech Detection Dataset (Binary)
* Link to publication: [https://arxiv.org/pdf/2006.08328.pdf](https://arxiv.org/pdf/2006.08328.pdf)
* Link to data: [https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset](https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset)
* Task description: Binary (Hate, Not)
* Details of task: Gender, Race, National Origin, Disability, Religion, Sexual Orientation
* Size of dataset: 998
* Percentage abusive: 0.43
* Language: English
* Level of annotation: Posts
* Platform: Youtube, Reddit
* Medium: Text
* Reference: Mollas, I., Chrysopoulou, Z., Karlos, S., and Tsoumakas, G., 2021. ETHOS: an Online Hate Speech Detection Dataset. Complex & Intelligent Systems, Jan. 2022

#### ETHOS: an Online Hate Speech Detection Dataset (Multi label)
* Link to publication: [https://arxiv.org/pdf/2006.08328.pdf](https://arxiv.org/pdf/2006.08328.pdf)
* Link to data: [https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset](https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset)
* Task description: 8 Categories (Violence, Directed/Undirected, Gender, Race, National Origin, Disability, Sexual Orientation, Religion)
* Details of task: Gender, Race, National Origin, Disability, Religion, Sexual Orientation
* Size of dataset: 433
* Percentage abusive: 0.33
* Language: English
* Level of annotation: Posts
* Platform: Youtube, Reddit
* Medium: Text
* Reference: Mollas, I., Chrysopoulou, Z., Karlos, S., and Tsoumakas, G., 2021. ETHOS: an Online Hate Speech Detection Dataset. Complex & Intelligent Systems, Jan. 2022

#### Twitter Sentiment Analysis
* Link to publication: NA
* Link to data: [https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech](https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech)
* Task description: Binary (Hate, Not)
* Details of task: Racism, Sexism
* Size of dataset: 31,961
* Percentage abusive: 0.07
* Language: English
* Level of annotation: Posts
* Platform: Twitter
* Medium: Text
* Reference: Ali Toosi, Jan 2019. Twitter Sentiment Analysis

#### Toxicity Detection: Does Context Really Matter? CAT-LARGE (No Context)
* Link to publication: [https://arxiv.org/pdf/2006.00998.pdf](https://arxiv.org/pdf/2006.00998.pdf)
* Link to data: [https://github.com/ipavlopoulos/context_toxicity](https://github.com/ipavlopoulos/context_toxicity)
* Task description: Binary (Toxic, Non-toxic)
* Details of task: Toxicity, Context
* Size of dataset: 10,000
* Percentage abusive: 0.006
* Language: English
* Level of annotation: Post 
* Platform: Wikipedia Talk Pages
* Medium: Text
* Reference: Pavlopoulos, J., Sorensen, J., Dixon, L., Thain, N., & Androutsopoulos, I. (2020). Toxicity Detection: Does Context Really Matter? ArXiv:2006.00998 [Cs].

#### Toxicity Detection: Does Context Really Matter? CAT-LARGE (With Context)
* Link to publication: [https://arxiv.org/pdf/2006.00998.pdf](https://arxiv.org/pdf/2006.00998.pdf)
* Link to data: [https://github.com/ipavlopoulos/context_toxicity](https://github.com/ipavlopoulos/context_toxicity)
* Task description: Binary (Toxic, Non-toxic)
* Details of task: Toxicity, Context
* Size of dataset: 10,000
* Percentage abusive: 0.02
* Language: English
* Level of annotation: Post 
* Platform: Wikipedia Talk Pages
* Medium: Text
* Reference: Pavlopoulos, J., Sorensen, J., Dixon, L., Thain, N., & Androutsopoulos, I. (2020). Toxicity Detection: Does Context Really Matter? ArXiv:2006.00998 [Cs].

#### Anatomy of Online Hate: Developing a Taxonomy and Machine Learning Models for Identifying and Classifying Hate in Online News Media 
* Link to publication: [https://www.aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/viewFile/17885/17024](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/viewFile/17885/17024)
* Link to data: [https://www.dropbox.com/s/21wtzy9arc5skr8/ICWSM18%20-%20SALMINEN%20ET%20AL.xlsx?dl=0](https://www.dropbox.com/s/21wtzy9arc5skr8/ICWSM18%20-%20SALMINEN%20ET%20AL.xlsx?dl=0)
* Task description:  Binary (Hate, Not), Multinomial classification (21 categories divided into 'hateful language', 'hate targets' and 'hate sub-targets') 
* Details of task: Group-directed + Person-directed
* Size of dataset: 5,143
* Percentage abusive: 82%
* Language: English 
* Level of annotation: Comment
* Platform: YouTube and Facebook
* Medium: Text
* Reference: Salminen, J., Almerekhi, H., Milenković, M., Jung, S., An, J., Kwak, H. and Jansen, B., 2018, Anatomy of Online Hate: Developing a Taxonomy and Machine Learning Models for Identifying and Classifying Hate in Online News Media, In: Proceedings of the Twelfth International AAAI Conference on Web and Social Media (ICWSM 2018), pp.330-339

<a id="Estonian-header"></a>
### Estonian
#### Automating News Comment Moderation with Limited Resources: Benchmarking in Croatian and Estonian
* Link to publication: [https://jlcl.org/content/2-allissues/1-heft1-2020/jlcl_2020-1_3.pdf](https://jlcl.org/content/2-allissues/1-heft1-2020/jlcl_2020-1_3.pdf)
* Link to data: [http://hdl.handle.net/11356/1401](http://hdl.handle.net/11356/1401)
* Task description: Binary (Deleted, Not) 
* Details of task: Flagged content performmed by the real newspaper moderators 
* Size of dataset: 31.5M 
* Percentage abusive: 12.5% 
* Language: Estonian (some in Russian also) 
* Level of annotation: Posts 
* Platform: Newspaper comments 
* Platform: Eesti Ekspress (www.ekspress.ee) website 
* Medium: Text 
* Reference: Ravi Shekhar, Marko Pranjić, Senja Pollak, Andraž Pelicon, Matthew Purver (2020). Automating News Comment Moderation with Limited Resources: Benchmarking in Croatian and Estonian. Journal for Language Technology and Computational Linguistics (JLCL). 


<a id="French-header"></a>
### French
#### CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (French)
* Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf](https://www.aclweb.org/anthology/P19-1271.pdf)
* Link to data: [https://github.com/marcoguerini/CONAN](https://github.com/marcoguerini/CONAN)
* Task description: Binary (Islamophobic / not), Multi-topic (Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic)
* Details of task: Islamophobia 
* Size of dataset: 1,719 
* Percentage abusive: 1 
* Language: French 
* Level of annotation: Posts 
* Platform: Synthetic / Facebook 
* Medium: Text 
* Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 


#### Multilingual and Multi-Aspect Hate Speech Analysis (French)
* Link to publication: [https://arxiv.org/abs/1908.11049](https://arxiv.org/abs/1908.11049)
* Link to data: [https://github.com/HKUST-KnowComp/MLMA_hate_speech](https://github.com/HKUST-KnowComp/MLMA_hate_speech)
* Task description: Detailed taxonomy with cross-cutting attributes: Hostility, Directness, Target Attribute, Target Group, How annotators felt on seeing the tweet. 
* Details of task: Gender, Sexual orientation, Religion, Disability 
* Size of dataset: 4,014 
* Percentage abusive: 0.72 
* Language: French 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. and Yeung, D., 2019. Multilingual and Multi-Aspect Hate Speech Analysis. ArXiv,. 

<a id="German-header"></a>
### German
#### RP-Mod & RP-Crowd: Moderator- and Crowd-Annotated German News Comment Datasets
* Link to publication: [https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/c9e1074f5b3f9fc8ea15d152add07294-Paper-round2.pdf](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/c9e1074f5b3f9fc8ea15d152add07294-Paper-round2.pdf)
* Link to data: [https://zenodo.org/record/5291339#.Ybr_9VkxkUE](https://zenodo.org/record/5291339#.Ybr_9VkxkUE)
* Task description: Binary (Offensive or Not), Multi-class/-label (sexism, racism, threats, insults, profane language, meta, advertisement).
* Details of task: The comments originate from a large German newspaper and are annotated by professional moderators (community managers). Additionally, each comment was further annotated by five different crowd-workers.
* Size of dataset: 85,000
* Percentage abusive: 8.4%
* Language: German
* Level of annotation: Comments 
* Platform: German Newspaper (Rheinische Post)
* Medium: Text 
* Reference: Assenmacher, D., Niemann, M., Müller, K., Seiler, M., Riehle, D. M., & Trautmann, H. (2021). RP-Mod & RP-Crowd: Moderator- and crowd-annotated german news comment datasets. In Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmark.

#### Measuring the Reliability of Hate Speech Annotations: The Case of the European Refugee Crisis
* Link to publication: [https://arxiv.org/pdf/1701.08118.pdf](https://arxiv.org/pdf/1701.08118.pdf)
* Link to data: [https://github.com/UCSM-DUE/IWG_hatespeech_public](https://github.com/UCSM-DUE/IWG_hatespeech_public)
* Task description: Binary (Anti-refugee hate, None) 
* Details of task: Refugees 
* Size of dataset: 469 
* Percentage abusive: NA 
* Language: German 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ross, B., Rist, M., Carbonell, G., Cabrera, B., Kurowsky, N. and Wojatzki, M., 2017. Measuring the Reliability of Hate Speech Annotations: The Case of the European Refugee Crisis. ArXiv,. 

#### Detecting Offensive Statements Towards Foreigners in Social Media
* Link to publication: [https://pdfs.semanticscholar.org/23dc/df7c7e82807445afd9f19474fc0a3d8169fe.pdf](https://pdfs.semanticscholar.org/23dc/df7c7e82807445afd9f19474fc0a3d8169fe.pdf)
* Link to data: [http://ub-web.de/research/](http://ub-web.de/research/)
* Task description: Hierarchical (Anti-foreigner prejudice, split into (1) slightly offensive/offensive and (2) explicitly/substantially offensive). 6 targets (Foreigner, Government, Press, Community, Other, Unknown)
* Details of task: Anti-foreigner prejudice 
* Size of dataset: 5,836 
* Percentage abusive: 0.11 
* Language: German 
* Level of annotation: Posts 
* Platform: Facebook 
* Medium: Text 
* Reference: Bretschneider, U. and Peters, R., 2017. Detecting Offensive Statements towards Foreigners in Social Media. In: Proceedings of the 50th Hawaii International Conference on System Sciences. 

#### GermEval 2018
 * Link to publication: [https://www.researchgate.net/publication/327914386_Overview_of_the_GermEval_2018_Shared_Task_on_the_Identification_of_Offensive_Language](https://www.researchgate.net/publication/327914386_Overview_of_the_GermEval_2018_Shared_Task_on_the_Identification_of_Offensive_Language)
* Link to data: [https://github.com/uds-lsv/GermEval-2018-Data](https://github.com/uds-lsv/GermEval-2018-Data)
* Task description: Branching structure: Binary (Offense, Other), 3 levels within Offense (Abuse, Insult, Profanity) 
* Details of task: Group-directed + Incivility 
* Size of dataset: 8,541 
* Percentage abusive: 0.34 
* Language: German 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Wiegand, M., Siegel, M. and Ruppenhofer, J., 2018. Overview of the GermEval 2018 Shared Task on the Identification of Offensive Language. In: Proceedings of GermEval 2018, 14th Conference on Natural Language Processing (KONVENS 2018). Vienna, Austria: Research Gate. 

#### Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages
* Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true](https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)
* Link to data: [https://hasocfire.github.io/hasoc/2019/dataset.html](https://hasocfire.github.io/hasoc/2019/dataset.html)
* Task description: A: Hate / Offensive or neither, B: Hatespeech, Offensive, or Profane 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 4,669 
* Percentage abusive: 0.24 
* Language: German 
* Level of annotation: Posts 
* Platform: Twitter and Facebook 
* Medium: Text 
* Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 

<a id="Greek-header"></a>
### Greek
#### Deep Learning for User Comment Moderation, Flagged Comments
* Link to publication: [https://www.aclweb.org/anthology/W17-3004](https://www.aclweb.org/anthology/W17-3004
https://www.aclweb.org/anthology/D17-1117)
* Link to data: [http://www.straintek.com/data/](http://www.straintek.com/data/)
* Task description: Binary (Flagged, Not) 
* Details of task: Flagged content 
* Size of dataset: 1,450,000 
* Percentage abusive: 0.34 
* Language: Greek 
* Level of annotation: Posts 
* Platform: Gazetta 
* Medium: text 
* Reference: Pavlopoulos, J., Malakasiotis, P. and Androutsopoulos, I., 2017. Deep Learning for User Comment Moderation. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.25-35. 

#### Deep Learning for User Comment Moderation, Moderated Comments
* Link to publication: [https://www.aclweb.org/anthology/W17-3004](https://www.aclweb.org/anthology/W17-3004)
* Link to data: [http://www.straintek.com/data/](http://www.straintek.com/data/)
* Task description: Binary (Flagged, Not) 
* Details of task: Flagged content 
* Size of dataset: 1,500 
* Percentage abusive: 0.22 
* Language: Greek 
* Level of annotation: Posts 
* Platform: Gazetta 
* Medium: text 
* Reference: Pavlopoulos, J., Malakasiotis, P. and Androutsopoulos, I., 2017. Deep Learning for User Comment Moderation. In: Proceedings of the First Workshop on Abusive Language Online. Vancouver, Canada: Association for Computational Linguistics, pp.25-35. 

#### Offensive Language Identification in Greek
* Link to publication: [https://arxiv.org/pdf/2003.07459v1.pdf](https://arxiv.org/pdf/2003.07459v1.pdf)
* Link to data: [https://sites.google.com/site/offensevalsharedtask/home](https://sites.google.com/site/offensevalsharedtask/home)
* Task description: Branching structure of tasks: Binary (Offensive, Not), Within Offensive (Target, Not), Within Target (Individual, Group, Other) 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 4779 
* Percentage abusive: 0.29 
* Language: Greek 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Pitenis, Z., Zampieri, M. and Ranasinghe, T., 2020. Offensive Language Identification in Greek. ArXiv. 

<a id="Hindi-header"></a>
### Hindi / Hindi-English
#### Hostility Detection Dataset in Hindi
* Link to publication: [https://arxiv.org/pdf/2011.03588.pdf](https://arxiv.org/pdf/2011.03588.pdf)
* Link to data: [https://competitions.codalab.org/competitions/26654](https://competitions.codalab.org/competitions/26654)
* Task description: Branching structure of tasks: Binary (Hostile, Not Hostile), Multi-tags within Hostile (Fake News, Hate, Offense, Defame) 
* Details of task: Hostility detection
* Size of dataset: 8,192 
* Percentage abusive: 47% 
* Language: Hindi
* Level of annotation: Posts
* Platform: Twitter, Facebook, WhatsApp
* Medium: Text 
* Reference: Bhardwaj, M., Akhtar, M.S., Ekbal, A., Das, A. and Chakraborty, T., 2020. Hostility detection dataset in hindi. arXiv preprint arXiv:2011.03588. 

#### Aggression-annotated Corpus of Hindi-English Code-mixed Data
* Link to publication: [https://arxiv.org/pdf/1803.09402](https://arxiv.org/pdf/1803.09402)
* Link to data: [https://github.com/kraiyani/Facebook-Post-Aggression-Identification](https://github.com/kraiyani/Facebook-Post-Aggression-Identification)
* Task description: 3 part hierachy for hate (None, Covert Aggression, Overt Aggression), 4 part target categorisation (Physical threat, Sexual threat, Identity threat, Non-threatening aggression), 3-part discursive role categorisation (Attack, Defend, Abet)
* Details of task: Numerous sub-categorizations 
* Size of dataset: 18,000 
* Percentage abusive: 0.06 
* Language: Hindi-English 
* Level of annotation: Posts 
* Platform: Facebook 
* Medium: Text 
* Reference: Kumar, R., Reganti, A., Bhatia, A. and Maheshwari, T., 2018. Aggression-annotated Corpus of Hindi-English Code-mixed Data. ArXiv,. 

#### Aggression-annotated Corpus of Hindi-English Code-mixed Data
* Link to publication: [https://arxiv.org/pdf/1803.09402](https://arxiv.org/pdf/1803.09402)
* Link to data: [https://github.com/kraiyani/Facebook-Post-Aggression-Identification](https://github.com/kraiyani/Facebook-Post-Aggression-Identification)
* Task description: 3 part hierachy for hate (None, Covert Aggression, Overt Aggression), 4 part target categorisation (Physical threat, Sexual threat, Identity threat, Non-threatening aggression), 3-part discursive role categorisation (Attack, Defend, Abet)
* Details of task: Numerous sub-categorizations 
* Size of dataset: 21,000 
* Percentage abusive: 0.27 
* Language: Hindi-English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Kumar, R., Reganti, A., Bhatia, A. and Maheshwari, T., 2018. Aggression-annotated Corpus of Hindi-English Code-mixed Data. ArXiv,. 
   
#### Did You Offend Me? Classification of Offensive Tweets in Hinglish Language
* Link to publication: [https://www.aclweb.org/anthology/W18-5118](https://www.aclweb.org/anthology/W18-5118)
* Link to data: [https://github.com/pmathur5k10/Hinglish-Offensive-Text-Classification](https://github.com/pmathur5k10/Hinglish-Offensive-Text-Classification)
* Task description: Hierarchy (Not Offensive, Abusive, Hate) 
* Details of task: Sexism 
* Size of dataset: 3,189 
* Percentage abusive: 0.65 
* Language: Hindi-English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Mathur, P., Sawhney, R., Ayyar, M. and Shah, R., 2018. Did you offend me? Classification of Offensive Tweets in Hinglish Language. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.138-148. 

#### A Dataset of Hindi-English Code-Mixed Social Media Text for Hate Speech Detection
* Link to publication: [https://www.aclweb.org/anthology/W18-1105](https://www.aclweb.org/anthology/W18-1105)
* Link to data: [https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text](https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text)
* Task description: Binary (Hate, Not) 
* Details of task: Hate per se 
* Size of dataset: 4,575 
* Percentage abusive: 0.36 
* Language: Hindi-English 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Bohra, A., Vijay, D., Singh, V., Sarfaraz Akhtar, S. and Shrivastava, M., 2018. A Dataset of Hindi-English Code-Mixed Social Media Text for Hate Speech Detection. In: Proceedings of the Second Workshop on Computational Modeling of People’s Opinions, Personality, and Emotions in Social Media. New Orleans, Louisiana: Association for Computational Linguistics, pp.36-41. 

#### Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages
* Link to publication: [https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true](https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)
* Link to data: [https://hasocfire.github.io/hasoc/2019/dataset.htm](https://hasocfire.github.io/hasoc/2019/dataset.html)
* Task description: A: Hate, Offensive or Neither, B: Hatespeech, Offensive, or Profane, C: Targeted or Untargeted 
* Details of task: Group-directed + Person-directed 
* Size of dataset: 5,983 
* Percentage abusive: 0.51 
* Language: Hindi 
* Level of annotation: Posts 
* Platform: Twitter and Facebook 
* Medium: Text 
* Reference: Mandl, T., Modha, S., Majumder, P., Patel, D., Dave, M., Mandlia, C. and Patel, A., 2019. Overview of the HASOC track at FIRE 2019. In: Proceedings of the 11th Forum for Information Retrieval Evaluation,. 

<a id="Indonesian-header"></a>
### Indonesian
#### Hate Speech Detection in the Indonesian Language: A Dataset and Preliminary Study
* Link to publication: [https://ieeexplore.ieee.org/document/8355039](https://ieeexplore.ieee.org/document/8355039)
* Link to data: [https://github.com/ialfina/id-hatespeech-detection](https://github.com/ialfina/id-hatespeech-detection)
* Task description: Binary (Hate, Not) 
* Details of task: Hate per se 
* Size of dataset: 713 
* Percentage abusive: 0.36 
* Language: Indonesian 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Alfina, I., Mulia, R., Fanany, M. and Ekanata, Y., 2017. Hate Speech Detection in the Indonesian Language: A Dataset and Preliminary Study. In: International Conference on Advanced Computer Science and Information Systems. pp.233-238. 


#### Multi-Label Hate Speech and Abusive Language Detection in Indonesian Twitter
* Link to publication: [https://www.aclweb.org/anthology/W19-3506](https://www.aclweb.org/anthology/W19-3506)
* Link to data: [https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection](https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection)
* Task description: (No hate speech, No hate speech but abusive, Hate speech but no abuse, Hate speech and abuse), within hate, category (Religion/creed, Race/ethnicity, Physical/disability, Gender/sexual orientation, Other invective/slander), within hate, strength (Weak, Moderate and Strong)
* Details of task: Religion, Race, Disability, Gender
* Size of dataset: 13,169 
* Percentage abusive: 0.42 
* Language: Indonesian 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Okky Ibrohim, M. and Budi, I., 2019. Multi-label Hate Speech and Abusive Language Detection in Indonesian Twitter. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.46-57. 

#### A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media
* Link to publication: [https://www.sciencedirect.com/science/article/pii/S1877050918314583](https://www.sciencedirect.com/science/article/pii/S1877050918314583)
* Link to data: [https://github.com/okkyibrohim/id-abusive-language-detection](https://github.com/okkyibrohim/id-abusive-language-detection)
* Task description: Hierarchical (Not abusive, Abusive but not offensive, Offensive) 
* Details of task: Incivility 
* Size of dataset: 2,016 
* Percentage abusive: 0.54 
* Language: Indonesian 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ibrohim, M. and Budi, I., 2018. A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media. Procedia Computer Science, 135, pp.222-229. 


<a id="Latvian-header"></a>
### Latvian
#### Latvian newspaper user comment dataset
* Link to publication: [https://aclanthology.org/2021.hackashop-1.14.pdf](https://aclanthology.org/2021.hackashop-1.14.pdf)
* Link to data: [https://www.clarin.si/repository/xmlui/handle/11356/1407](https://www.clarin.si/repository/xmlui/handle/11356/1407)
* Task description: Binary (Deleted, Not) 
* Details of task: Flagged content performmed by the real newspaper moderators 
* Size of dataset: 12M 
* Percentage abusive: ~10% 
* Language: Latvian 
* Level of annotation: Posts 
* Platform: Newspaper comments 
* Medium: Text 
* Reference: Senja Pollak, Marko Robnik-Šikonja, Matthew Purver, Michele Boggia, Ravi Shekhar, Marko Pranjić, Salla Salmela, Ivar Krustok, Tarmo Paju, Carl-Gustav Linden, Leo Leppänen, Elaine Zosa, Matej Ulčar, Linda Freiental, Silver Traat, Luis Adrián Cabrera-Diego, Matej Martinc, Nada Lavrač, Blaž Škrlj, Martin Žnidaršič, Andraž Pelicon, Boshko Koloski, Vid Podečan, Janez Kranjc, Shane Sheehan, Emanuela Boros, Jose Moreno, Antoine Doucet, Hannu Toivonen (2021). EMBEDDIA Tools, Datasets and Challenges: Resources and Hackathon Contributions. Proceedings of the Hackashop on News Media Content Analysis and Automated Report Generation (EACL). 


<a id="Italian-header"></a>
### Italian
#### An Italian Twitter Corpus of Hate Speech against Immigrants
* Link to publication: [https://www.aclweb.org/anthology/L18-1443](https://www.aclweb.org/anthology/L18-1443)
* Link to data: [https://github.com/msang/hate-speech-corpus](https://github.com/msang/hate-speech-corpus)
* Task description: Binary (Immigrants/Roma/Muslims, Not), additional categories. Within Hate, Intensity measurement (Aggressiveness: No, Weak, Strong, Offensiveness: No, Weak, Strong, Irony: No, Yes, Stereotype: No, Yes, Incitement degree: 0-4) 
* Details of task: Immigrants, Roma and Muslims + numerous sub-categorizations
* Size of dataset: 1,827 
* Percentage abusive: 0.13 
* Language: Italian 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Sanguinetti, M., Poletto, F., Bosco, C., Patti, V. and Stranisci, M., 2018. An Italian Twitter Corpus of Hate Speech against Immigrants. In: Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018). Miyazaki, Japan: European Language Resources Association (ELRA). 
  
#### Overview of the EVALITA 2018 Hate Speech Detection Task (Facebook)
* Link to publication: [http://ceur-ws.org/Vol-2263/paper010.pdf](http://ceur-ws.org/Vol-2263/paper010.pdf)
* Link to data: [http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html](http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html)
* Task description: Binary (Hate, Not), Within hate for Facebook only, strength (No hate, Weak hate, Strong hate) and theme ((1) religion, (2) physical and/or mental handicap, (3) socio-economic status, (4) politics, (5) race, (6) sex and gender, (7) Other) 
* Details of task: Religion, physical and/or mental handicap, socio-economic status, politics, race, sex and gender 
* Size of dataset: 4,000 
* Percentage abusive: 0.51 
* Language: Italian 
* Level of annotation: Posts 
* Platform: Facebook 
* Medium: Text 
* Reference: Bosco, C., Dell'Orletta, F. and Poletto, F., 2018. Overview of the EVALITA 2018 Hate Speech Detection Task. In: EVALITA 2018-Sixth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. CEUR, pp.1-9. 


#### Overview of the EVALITA 2018 Hate Speech Detection Task (Twitter)
* Link to publication: [http://ceur-ws.org/Vol-2263/paper010.pdf](http://ceur-ws.org/Vol-2263/paper010.pdf)
* Link to data: [http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html](http://www.di.unito.it/~tutreeb/haspeede-evalita18/data.html) 
* Task description: Binary (Hate, Not), Within Hate For Twitter only Intensity (1-4 rating), Aggressiveness (No, Weak, Strong), Offensiveness (No, Weak, Strong), Irony (Yes, No) 
* Details of task: Group-directed 
* Size of dataset: 4,000 
* Percentage abusive: 0.32 
* Language: Italian 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Bosco, C., Dell'Orletta, F. and Poletto, F., 2018. Overview of the EVALITA 2018 Hate Speech Detection Task. In: EVALITA 2018-Sixth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. CEUR, pp.1-9. 

#### CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (Italian)
* Link to publication: [https://www.aclweb.org/anthology/P19-1271.pdf](https://www.aclweb.org/anthology/P19-1271.pdf)
* Link to data: [https://github.com/marcoguerini/CONAN](https://github.com/marcoguerini/CONAN)
* Task description: Binary (Islamophobic, Not), Multi-topic (Culture, Economics, Crimes, Rapism, Terrorism, Women Oppression, History, Other/generic)
* Details of task: Islamophobia 
* Size of dataset: 1,071 
* Percentage abusive: 1 
* Language: Italian 
* Level of annotation: Posts 
* Platform: Synthetic / Facebook 
* Medium: Text 
* Reference: Chung, Y., Kuzmenko, E., Tekiroglu, S. and Guerini, M., 2019. CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, pp.2819-2829. 


#### Creating a WhatsApp Dataset to Study Pre-teen Cyberbullying
* Link to publication: [https://www.aclweb.org/anthology/W18-5107](https://www.aclweb.org/anthology/W18-5107)
* Link to data: [https://github.com/dhfbk/WhatsApp-Dataset](https://github.com/dhfbk/WhatsApp-Dataset)
* Task description: Binary (Cyberbullying, Not) 
* Details of task: Person-directed 
* Size of dataset: 14,600 
* Percentage abusive: 0.08 
* Language: Italian 
* Level of annotation: Posts, structured into 10 chats, with token level information 
* Platform: Synthetic / Whatsapp 
* Medium: Text 
* Reference: Sprugnoli, R., Menini, S., Tonelli, S., Oncini, F. and Piras, E., 2018. Creating a WhatsApp Dataset to Study Pre-teen Cyberbullying. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2) Month: October. Brussels, Belgium: Association for Computational Linguistics, pp.51-59. 

<a id="Polish-header"></a>
### Polish
#### Results of the PolEval 2019 Shared Task 6:First Dataset and Open Shared Task for Automatic Cyberbullying Detection in Polish Twitter
* Link to publication: [http://poleval.pl/files/poleval2019.pdf](http://poleval.pl/files/poleval2019.pdf)
* Link to data: [http://poleval.pl/tasks/task6](http://poleval.pl/tasks/task6)
* Task description: Harmfulness score (three values), Multilabel from seven phenomena
* Details of task: Person-directed 
* Size of dataset: 10,041 
* Percentage abusive: 0.09 
* Language: Polish 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Ogrodniczuk, M. and Kobyliński, L., 2019. Results of the PolEval 2019 Shared Task 6: First Dataset and Open Shared Task for Automatic Cyberbullying Detection in Polish Twitter. In: Proceedings of the PolEval 2019 Workshop. Warszawa: Institute of Computer Science, Polish Academy of Sciences. 

<a id="Portuguese-header"></a>
### Portuguese
#### A Hierarchically-Labeled Portuguese Hate Speech Dataset
* Link to publication: [https://www.aclweb.org/anthology/W19-3510](https://www.aclweb.org/anthology/W19-3510)
* Link to data: [https://b2share.eudat.eu/records/9005efe2d6be4293b63c3cffd4cf193e](https://b2share.eudat.eu/records/9005efe2d6be4293b63c3cffd4cf193e)
* Task description: Binary (Hate, Not), Multi-level (81 categories, identified inductively; categories have different granularities and content can be assigned to multiple categories at once) 
* Details of task: Multiple identities inductively categorized 
* Size of dataset: 3,059 
* Percentage abusive: 0.32 
* Language: Portuguese 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Fortuna, P., Rocha da Silva, J., Soler-Company, J., Warner, L. and Nunes, S., 2019. A Hierarchically-Labeled Portuguese Hate Speech Dataset. In: Proceedings of the Third Workshop on Abusive Language Online. Florence, Italy: Association for Computational Linguistics, pp.94-104. 

#### Offensive Comments in the Brazilian Web: A Dataset and Baseline Results
* Link to publication: [http://www.each.usp.br/digiampietri/BraSNAM/2017/p04.pdf](http://www.each.usp.br/digiampietri/BraSNAM/2017/p04.pdf)
* Link to data: [https://github.com/rogersdepelle/OffComBR](https://github.com/rogersdepelle/OffComBR)
* Task description: Binary (Offensive, Not), Target (Xenophobia, homophobia, sexism, racism, cursing, religious intolerance) 
* Details of task: Religion/creed, Race/ethnicity, Physical/disability, Gender/sexual orientation 
* Size of dataset: 1,250 
* Percentage abusive: 0.33 
* Language: Portuguese 
* Level of annotation: Posts 
* Platform: g1.globo.com 
* Medium: Text 
* Reference: de Pelle, R. and Moreira, V., 2017. Offensive Comments in the Brazilian Web: A Dataset and Baseline Results. In: VI Brazilian Workshop on Social Network Analysis and Mining. SBC. 

<a id="Russian-header"></a>
### Russian
#### Reducing Unintended Identity Bias in Russian Hate Speech Detection
* Link to publication: [https://aclanthology.org/2020.alw-1.8.pdf](https://aclanthology.org/2020.alw-1.8.pdf)
* Link to data: License Required (Last checked 17/01/2022)
* Task description: Binary (Hate, Not)
* Details of task: Toxicity, Harassment, Sexism, Homophobia, Nationalism
* Size of dataset: 100,000
* Percentage abusive: NA
* Language: Russian
* Level of annotation: Posts 
* Platform: Youtube
* Medium: Text
* Reference: Zueva, Nadezhda, et al, Oct. 2020. Reducing Unintended Identity Bias in Russian Hate Speech Detection. In: Proceedings of the Fourth Workshop on Online Abuse and Harms, pages 65–69

#### Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages
* Link to publication: [https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf](https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf)
* Link to data: [https://github.com/bohdan1/AbusiveLanguageDataset](https://github.com/bohdan1/AbusiveLanguageDataset)
* Task description: Binary (True == Abusive, False == Not)
* Details of task: Multilingual, Abusive Words, Political
* Size of dataset: 2,000
* Percentage abusive: 0.33
* Language: Surzhyk (Russian & Ukranian)
* Level of annotation: Posts 
* Platform: Youtube
* Medium: Text
* Reference: Andrusyak, B., Rimel, M. and Kern, R., 2018. Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages. In: Proceedings of Recent Advances in Slavonic Natural Language Processing, RASLAN 2018, pp. 77–84, 2018. 

#### Russian South Park
* Link to publication: [https://aclanthology.org/2021.bsnlp-1.3/](https://aclanthology.org/2021.bsnlp-1.3/)
* Link to data: [https://github.com/Sariellee/Russan-Hate-speech-Recognition](https://github.com/Sariellee/Russan-Hate-speech-Recognition)
* Task description: Binary (abusive, non-abusive)
* Details of task: Abusive language in Russian South Park scripts
* Size of dataset: 1400
* Percentage abusive: 22.2%
* Language: Russian
* Level of annotation: Sentence
* Platform: TV Subtitles
* Medium: text 
* Reference: Saitov & Derczynski, 2021. "Abusive Language Recognition in Russian". Proceedings of the 8th BSNLP Workshop on Balto-Slavic Natural Language Processing, ACL


<a id="Slovene-header"></a>
### Slovene
#### Datasets of Slovene and Croatian Moderated News Comments
* Link to publication: [https://www.aclweb.org/anthology/W18-5116](https://www.aclweb.org/anthology/W18-5116)
* Link to data: [http://hdl.handle.net/11356/1201](http://hdl.handle.net/11356/1201)
* Task description: Binary (Deleted, Not) 
* Details of task: Flagged content 
* Size of dataset: 7,600,000 
* Percentage abusive: 0.08 
* Language: Slovene 
* Level of annotation: Posts 
* Platform: MMC RTV website 
* Medium: Text 
* Reference: Ljubešić, N., Erjavec, T. and Fišer, D., 2018. Datasets of Slovene and Croatian Moderated News Comments. In: Proceedings of the 2nd Workshop on Abusive Language Online (ALW2). Brussels, Belgium: Association for Computational Linguistics, pp.124-131. 
  
<a id="Spanish-header"></a>
### Spanish
#### Overview of MEX-A3T at IberEval 2018: Authorship and Aggressiveness Analysis in Mexican Spanish Tweets
* Link to publication: [http://ceur-ws.org/Vol-2150/overview-mex-a3t.pdf](http://ceur-ws.org/Vol-2150/overview-mex-a3t.pdf)
* Link to data: [https://mexa3t.wixsite.com/home/aggressive-detection-track](https://mexa3t.wixsite.com/home/aggressive-detection-track)
* Task description: Binary (Aggressive, Not) 
* Details of task: Group-directed 
* Size of dataset: 11,000 
* Percentage abusive: 0.32 
* Language: Spanish 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Alvarez-Carmona, M., Guzman-Falcon, E., Montes-y-Gomez, M., Escalante, H., Villasenor-Pineda, L., Reyes-Meza, V. and Rico-Sulayes, A., 2018. Overview of MEX-A3T at IberEval 2018: Authorship and aggressiveness analysis in Mexican Spanish tweets. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 

#### Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (Spanish)
* Link to publication: [http://ceur-ws.org/Vol-2150/overview-AMI.pdf](http://ceur-ws.org/Vol-2150/overview-AMI.pdf)
* Link to data: [https://amiibereval2018.wordpress.com/important-dates/data/](https://amiibereval2018.wordpress.com/important-dates/data/) 
* Task description: Binary (Misogyny, Not), 5 categories (Stereotype, Dominance, Derailing, Sexual harassment, Discredit), Target of misogyny (Active or Passive) 
* Details of task: Sexism 
* Size of dataset: 4,138 
* Percentage abusive: 0.5 
* Language: Spanish 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Fersini, E., Rosso, P. and Anzovino, M., 2018. Overview of the Task on Automatic Misogyny Identification at IberEval 2018. In: Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018). 

#### hatEval, SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter (Spanish)
* Link to publication: [https://www.aclweb.org/anthology/S19-2007](https://www.aclweb.org/anthology/S19-2007)
* Link to data: [competitions.codalab.org/competitions/19935](competitions.codalab.org/competitions/19935)
* Task description: Branching structure of tasks: Binary (Hate, Not), Within Hate (Group, Individual), Within Hate (Agressive, Not)
* Details of task: Group-directed + Person-directed 
* Size of dataset: 6,600 
* Percentage abusive: 0.4 
* Language: Spanish 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Basile, V., Bosco, C., Fersini, E., Nozza, D., Patti, V., Pardo, F., Rosso, P. and Sanguinetti, M., 2019. SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter. In: Proceedings of the 13th International Workshop on Semantic Evaluation. Minneapolis, Minnesota: Association for Computational Linguistics, pp.54-63. 

<a id="Turkish-header"></a>
### Turkish
#### A Corpus of Turkish Offensive Language on Social Media
* Link to publication: [https://coltekin.github.io/offensive-turkish/troff.pdf](https://coltekin.github.io/offensive-turkish/troff.pdf)
* Link to data: [https://sites.google.com/site/offensevalsharedtask/home](https://sites.google.com/site/offensevalsharedtask/home) 
* Task description: Branching structure of tasks: Binary (Hate, Not), Within Hate (Group, Individual), Within Hate (Agressive, Not)
* Details of task: Group-directed + Person-directed 
* Size of dataset: 36232 
* Percentage abusive: 0.19 
* Language: Turkish 
* Level of annotation: Posts 
* Platform: Twitter 
* Medium: Text 
* Reference: Çöltekin, C., 2020. A Corpus of Turkish Offensive Language on Social Media. In: Proceedings of the 12th International Conference on Language Resources and Evaluation. 

<a id="Ukranian-header"></a>
### Ukranian
#### Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages
* Link to publication: [https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf](https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf)
* Link to data: [https://github.com/bohdan1/AbusiveLanguageDataset](https://github.com/bohdan1/AbusiveLanguageDataset)
* Task description: Binary (True == Abusive, False == Not)
* Details of task: Multilingual, Abusive Words, Political
* Size of dataset: 2,000
* Percentage abusive: 0.33
* Language: Surzhyk (Russian & Ukranian)
* Level of annotation: Posts 
* Platform: Youtube
* Medium: Text
* Reference: Andrusyak, B., Rimel, M. and Kern, R., 2018. Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages. In: Proceedings of Recent Advances in Slavonic Natural Language Processing, RASLAN 2018, pp. 77–84, 2018. 


---
<a id="Keywords-header"></a>
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
   * You can also use the GATE abuse tagger, available at [https://cloud.gate.ac.uk/shopfront/displayItem/gate-hate](https://cloud.gate.ac.uk/shopfront/displayItem/gate-hate)

1. __Wiegand et al.__
   * Data link: [https://github.com/uds-lsv/lexicon-of-abusive-words](https://github.com/uds-lsv/lexicon-of-abusive-words)
   * Reference: [Inducing a Lexicon of Abusive Words – A Feature-Based Approach](https://www.aclweb.org/anthology/N18-1095.pdf), Proc. NAACL-HLT 2018

1. __Chandrasekharan et al.__
   * Data link: [Reddit hate lexicon](https://www.dropbox.com/sh/5ud4fwxvb6q7k20/AAAH_SN8i5cfmJRKJteEW2b2a?dl=0)
   * Reference: [You can't stay here: the efficacy of Reddit's 2015 ban examined through hate speech](http://comp.social.gatech.edu/papers/cscw18-chand-hate.pdf), Proc. ACL Hum-Comput Interact. 

<a id="Contributing-header"></a>
# How to Contribute

We accept entries to our catalogue based on pull requests to the `README.md` file. The dataset must be avaliable for download to be included in the list.
If you want to add an entry, follow these steps!
* Go to the README.md file and click the edit button in the top right corner of the file.


<img width="1239" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/22522221/150790020-ecbc6eea-3cf1-4134-ad51-a8a6334cfc2f.png">


* Edit the markdown file. Please first go the correct language. The items are then sorted by their publication date (newest first). Add your item by copy and pasting the following template and adding all the details:


```
#### Title
* Link to publication: [url](url) - link to the documentation and/or a data statement about the data
* Link to data: [url](url) - direct download is preferred, e.g. a link straight to a .zip file
* Task description: How the task is framed in this data, e.g. "Binary (Hate, Not)", "Hierarchical", "Three-class (Hate speech, Offensive language, None)"
* Details of task: Free-text description of the task this data models, e.g. "Misogyny detection on social media in Danish"
* Size of dataset: Give the number of instances of abusive/non-abusive/other items
* Percentage abusive: e.g. 1.2%
* Language: e.g. Arabic
* Level of annotation: What is an "instance", in this dataset? e.g. Posts, User, Conversation, ... 
* Platform: e.g. twitter, snapchat, ..
* Medium: text / image / audio / ...
* Reference: Give a bibliographic reference for the data (if there is one), with title, author, year, venue etc
```

* Check the “Preview Changes” tab to confirm everything is good to go!
* If you’re ready to submit, propose the changes. Make sure you give some brief detail on the proposed change.

<img width="1243" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/22522221/150790254-c4c004cb-567d-4401-95ba-7b7be6de53fd.png">

* Submit the pull request on the next page when prompted.

---

This page is [http://hatespeechdata.com/](http://hatespeechdata.com/).
