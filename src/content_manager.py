"""
Comprehensive Content Manager for Quran Institute Website
Contains all content for pages in both English and Arabic
"""

class ContentManager:
    def __init__(self):
        self.content = {
            'en': {
                'home': {
                    'title': 'International Computing Institute for Quran and Islamic Sciences',
                    'subtitle': 'A global leadership and reference in computing the Holy Quran, Islamic sciences and the Arabic language',
                    'mission': 'Establishing and developing a solid scientific reference for computing the Holy Quran, Islamic sciences and the Arabic language, and developing research, specialized scientific studies, computer programs and websites in this field, through distinguished and sustainable institutional work, and in cooperation and coordination with institutions and individuals specialized in computer, legal and linguistic fields; Which achieves an integrated vision and distinct outputs.',
                    'vision': 'A global leadership and reference in computing the Holy Quran, Islamic sciences and the Arabic language',
                    'objectives': [
                        'Establishing a digital scientific reference for computer data and information related to the Holy Quran, Islamic sciences, the Arabic language, and everything related to it.',
                        'Forming an umbrella for researchers and professionals interested in computing the Noble Quran, Islamic sciences and the Arabic language, to coordinate efforts among them.',
                        'Establishing scientific partnerships between specialists from individuals and institutions concerned with computing the Noble Quran, forensic sciences, the Arabic language, and related sciences.',
                        'Setting standards and controls for data that are dealt with in the fields of computing the Holy Quran, Islamic sciences and the Arabic language in order to reach correct and accurate scientific results.',
                        'Developing and training researchers and those interested in computing the Noble Quran, Islamic sciences and the Arabic language, while preparing methodological and exemplary training materials.',
                        'Opening channels of communication with different disciplines of scientific, legal, literary and others to serve the computerization of the Holy Quran, Islamic sciences and the Arabic language, and explores the points of intersection between them, and identifies the intersectional research that serves them.',
                        'Encouraging scientific research in the fields of computing the Noble Quran, Islamic sciences and the Arabic language, and providing research topics, development ideas and technical solutions to researchers and specialists in these fields.',
                        'Dissemination of knowledge and public awareness of the results of research in computing the Holy Quran, Islamic sciences and the Arabic language in an easy and accessible way.',
                        'Encouraging researchers and institutions concerned with computing the Noble Quran, Islamic sciences and the Arabic language to further their scientific and electronic productions with open source software.'
                    ]
                },
                'institute': {
                    'mission': {
                        'title': 'Mission',
                        'content': 'Establishing and developing a solid scientific reference for computing the Holy Quran, Islamic sciences and the Arabic language, and developing research, specialized scientific studies, computer programs and websites in this field, through distinguished and sustainable institutional work, and in cooperation and coordination with institutions and individuals specialized in computer, legal and linguistic fields; Which achieves an integrated vision and distinct outputs.'
                    },
                    'vision': {
                        'title': 'Vision', 
                        'content': 'A global leadership and reference in computing the Holy Quran, Islamic sciences and the Arabic language'
                    },
                    'board': {
                        'title': 'Board of Directors',
                        'members': [
                            {'name': 'Prof. Mohammed Zeki Khedher', 'position': 'President'},
                            {'name': 'Eng. Mohammad M. Khair', 'position': 'CEO'},
                            {'name': 'Dr. Majdi Sawalha', 'position': 'CTO'},
                            {'name': 'Prof. Akram Zeki', 'position': 'CIO'},
                            {'name': 'Dr. Mustafa AbuZuraidah', 'position': 'COO/Secretary'},
                            {'name': 'Eng. Mohammad M. Khair', 'position': 'CFO/Treasurer'},
                            {'name': 'Dr. Majdi Sawalha', 'position': 'VP, Educational Services'},
                            {'name': 'Prof. Dr. Yasser AlTarshany', 'position': 'Director'},
                            {'name': 'Dr. Mohammed Hameed Al-Tai', 'position': 'Director'},
                            {'name': 'Dr. Mohammad Sharaf ElDin Muftah', 'position': 'Director'}
                        ]
                    },
                    'bylaws': {
                        'title': 'Bylaws',
                        'content': 'The Institute operates under comprehensive bylaws that govern its activities, membership, and organizational structure. These bylaws ensure transparency, accountability, and adherence to Islamic principles in all our operations.'
                    },
                    'policy': {
                        'title': 'Policies',
                        'content': 'Our policies are designed to maintain the highest standards of academic integrity, research ethics, and Islamic values. We are committed to fostering an inclusive environment that promotes excellence in computational Islamic studies.'
                    },
                    'documents': {
                        'title': 'Official Documents',
                        'bylaws_section': {
                            'title': 'Institute Bylaws',
                            'links': [
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_English',
                                    'url': 'https://drive.google.com/file/d/1Tt3RCHs8H0d1C54pLo2QkXDMLCL0xUnT/view?usp=drive_link'
                                },
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_French',
                                    'url': 'https://drive.google.com/file/d/16ORKC72Ia4IBRwVNDJbTRSIYFhZIRpss/view?usp=drive_link'
                                },
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_Arabic_نظام الدستور للمعهد',
                                    'url': 'https://drive.google.com/file/d/1UX8VZCOuvGGQnguGKIcKqVWf1Qe9nf35/view?usp=drive_link'
                                }
                            ]
                        },
                        'policies_section': {
                            'title': 'Conflict of Interest Policies',
                            'links': [
                                {
                                    'title': 'Conflict Of Interest Policy v1 - English',
                                    'url': 'https://drive.google.com/file/d/1FgT-2X7c5PKkR_BlgOKuRZxoFAj1CeIA/view?usp=drive_link'
                                },
                                {
                                    'title': 'Conflict Of Interest Policy v1 - French',
                                    'url': 'https://drive.google.com/file/d/1hfk_mjOKDslQTJkNoES236rfpoA4lq6a/view?usp=drive_link'
                                },
                                {
                                    'title': 'Conflict Of Interest Policy v1 - Arabic - سياسة تعارض المصالح',
                                    'url': 'https://drive.google.com/file/d/1A57AnKooMyzD7NNY0HkRWkyP25prpv9Y/view?usp=sharing'
                                }
                            ]
                        },
                        'profile_section': {
                            'title': 'Institute Profile',
                            'links': [
                                {
                                    'title': 'The Institute Profile - الملف التعريفي للمعهد v1',
                                    'url': 'https://drive.google.com/file/d/12PwULyGOLJ_ih3N4z5uatrpRJiMMmTRK/view?usp=drive_link'
                                }
                            ]
                        }
                    }
                },
                'activities': {
                    'title': 'Activities and Societies',
                    'sections': [
                        {
                            'title': 'Availability of Resources',
                            'content': 'The Institute seeks to provide the space and tools that facilitate, support and integrate the efforts of researchers into the proposed research plans. The resources may be represented by computers or database servers that contain an indexed, accurate and documented representation of the Holy Quran texts in particular and Islamic sources in general, adding tools or packages for general purposes for data analysis. It can provide resources in a shared cloud to host the various systems created by researchers in the field.'
                        },
                        {
                            'title': 'Organizing Conferences, Workshops and Meetings',
                            'content': 'The Institute seeks to hold conferences and workshops in the field of research that fall within the interests of the Institute, regionally, internationally, in person and electronically. The institute also aims to be the engine for holding meetings between researchers interested in research in the same topic, through online meetings.'
                        },
                        {
                            'title': 'Publications',
                            'content': 'With the expected growth of the community interested in the proposed research plans, there will be a need to provide publishing media from scientific journals and methods of dissemination of knowledge necessary to provide a suitable environment for scientific research. The Institute also strives to provide high quality and accurate publications after review and audit.'
                        },
                        {
                            'title': 'Financial Support and Donations',
                            'content': 'The Institute announces its work plans in order to provide financial resources to contribute to supporting researchers and students in their research, build scientific platforms and provide the necessary hardware, software and cloud resources to host the various systems of scientific and technical software packages and other services. Therefore, the Institute accepts financial and in-kind donations that serve its objectives in general or for a specific project and monitors the disbursement of funds accurately and transparently within the controls stipulated in the Institute\'s founding regulations.'
                        },
                        {
                            'title': 'Investment Activities',
                            'content': 'The Institute may carry out an investment activity in electronic or other transactions for the purpose of financial support for the Institute\'s activity, provided that this does not exceed the percentage of the limits stipulated in the Institute\'s founding documents and in accordance with Islamic transactions permitted in Islamic Sharia.'
                        },
                        {
                            'title': 'Commercial Partnerships and Applications',
                            'content': 'As the data, information and software related to the Institute\'s activity can take their way to practical application through commercial, professional or scientific companies and institutions; The Institute will be open to contracting, cooperation and participation in electronic applications, whether educational or service-related to the Institute\'s interests, such as companies and institutions, within controls being studied in a way that does not conflict with the founding documents of the Institute.'
                        },
                        {
                            'title': 'Open Source Software',
                            'content': 'The institute seeks that the software it works on be open source as much as possible, with the aim of developing its work and encouraging cooperation and participation in the progress of mankind, without any kind of monopoly by certain companies and institutions, and considering such activity is preferable compared to non-open source software.'
                        },
                        {
                            'title': 'Electronic Endowment Management',
                            'content': 'The Institute accepts on behalf of individuals, institutions and associations that monitor endowments, as it manages them according to the conditions of the endowers, which are in the service of computing the Holy Quran, Islamic sciences and the Arabic language. In the endowment documents, and in a manner that does not contradict the articles of association of the Institute.'
                        },
                        {
                            'title': 'Professional Support and Development',
                            'content': 'The Institute aims to support undergraduate and graduate students interested in proposed research plans and facilitate possible scholarship opportunities. Furthermore, the Institute is committed to striving to develop the capabilities of its faculty, researchers, and working professionals as they advance in their careers. The Institute supports the process of promoting the proposed research plans as a career path and a path to success in academic and professional life, building a scientific platform for training and providing solutions and specialized technical expertise for all researchers and scholars.'
                        },
                        {
                            'title': 'Academic Degrees and Programs',
                            'content': 'In the coming years, the Institute seeks to develop academic programs for the bachelor\'s, master\'s and doctoral levels, specialized in computing the Holy Quran and Islamic sciences. It also seeks accreditation of these academic programs from international institutions that grant international accreditation to academic programs such as ABET in engineering, computer science, and others.'
                        }
                    ]
                },
                'training': {
                    'title': 'Training Programs',
                    'description': 'The Institute offers comprehensive training programs designed to bridge the gap between technology and Islamic sciences.',
                    'courses': [
                        {
                            'title': 'Introduction to Islamic and Linguistic Sciences for Technical Specialists',
                            'description': 'This course is designed for technical specialists who want to understand Islamic and linguistic sciences. It provides foundational knowledge necessary for developing computational applications in Islamic studies, covering essential concepts in Islamic jurisprudence, Arabic linguistics, and Quranic studies.'
                        },
                        {
                            'title': 'Information Technology Course in the Service of Islamic Sciences',
                            'description': 'This comprehensive course focuses on applying modern information technology to serve Islamic sciences. Participants will learn about database design for Islamic texts, natural language processing for Arabic, digital preservation of Islamic manuscripts, and development of Islamic educational software.'
                        }
                    ]
                },
                'projects': {
                    'title': 'Research Projects',
                    'content': 'Our institute is involved in various cutting-edge research projects that combine computational methods with Islamic studies. These projects include digital Quran analysis tools, Islamic manuscript digitization, Arabic natural language processing, and educational software for Islamic studies. We collaborate with international institutions to advance the field and provide valuable tools for researchers and scholars worldwide.'
                },
                'news': {
                    'title': 'Latest News',
                    'content': 'Stay updated with the latest developments, announcements, and achievements from the International Computing Institute for Quran and Islamic Sciences. We regularly publish updates about our research progress, upcoming conferences, training programs, and collaborative initiatives.',
                    'links': [
                        {
                            'title': 'Institute Activities',
                            'url': 'https://drive.google.com/file/d/19LGkjPZJDAQLQVDP47ns_aFca-YBaKuI/view?usp=sharing'
                        },
                        {
                            'title': 'الإجتماع السنوي الثاني - المعهد العالمي لحوسبة القرآن والعلوم الإسلامية -2024-05-25 (B)',
                            'url': 'https://drive.google.com/file/d/1XBxblr8iVJSUIbkh4BL-U17wueTBXKfk/view?usp=drive_link'
                        },
                        {
                            'title': 'YouTube Video Channel',
                            'url': 'https://www.youtube.com/@qurancomputing7916',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png'
                        },
                        {
                            'title': 'X (Twitter)',
                            'url': 'https://twitter.com/QuranComputing',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg'
                        },
                        {
                            'title': 'Facebook',
                            'url': 'https://www.facebook.com/QuranComputing/',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg'
                        }
                    ]
                },
                'members': {
                    'title': 'Members',
                    'content': 'Our institute brings together a diverse community of researchers, scholars, and professionals from around the world. Our members include computer scientists, Islamic scholars, linguists, and educators who share a common goal of advancing computational Islamic studies.'
                },
                'contact': {
                    'title': 'Contact Us',
                    'email': 'info@qurancomputing.org',
                    'content': 'We welcome inquiries, collaborations, and suggestions. Please feel free to contact us for any questions or opportunities for partnership. Our team is always ready to assist researchers, students, and institutions interested in computational Islamic studies.'
                },
                'donations': {
                    'title': 'Donations',
                    'content': 'The International Computing Institute for Quran and Islamic Sciences is a US Nonprofit Organization 501(c)(3) Tax Exempt EIN 88-1219520. For Direct Bank Transfer please email us at info@qurancomputing.org',
                    'donation_links': [
                        {
                            'title': 'Visa or MasterCard',
                            'url': 'https://donate.stripe.com/dR616G9Uk7C78WA5kk'
                        },
                        {
                            'title': 'Paypal',
                            'url': 'https://www.paypal.me/qurancomputing'
                        }
                    ]
                }
            },
            'ar': {
                'home': {
                    'title': 'المعهد العالمي لحوسبة القرآن والعلوم الإسلامية',
                    'subtitle': 'قيادة عالمية ومرجعية في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية',
                    'mission': 'إنشاء وتطوير مرجعية علمية راسخة لحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، وتطوير البحوث والدراسات العلمية المتخصصة والبرامج الحاسوبية والمواقع الإلكترونية في هذا المجال، من خلال عمل مؤسسي متميز ومستدام، وبالتعاون والتنسيق مع المؤسسات والأفراد المتخصصين في المجالات الحاسوبية والشرعية واللغوية؛ مما يحقق رؤية متكاملة ومخرجات متميزة.',
                    'vision': 'قيادة عالمية ومرجعية في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية',
                    'objectives': [
                        'إنشاء مرجعية علمية رقمية للبيانات والمعلومات الحاسوبية المتعلقة بالقرآن الكريم والعلوم الإسلامية واللغة العربية وكل ما يتعلق بها.',
                        'تكوين مظلة للباحثين والمهنيين المهتمين بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، لتنسيق الجهود فيما بينهم.',
                        'إقامة شراكات علمية بين المختصين من الأفراد والمؤسسات المعنية بحوسبة القرآن الكريم والعلوم الشرعية واللغة العربية والعلوم ذات الصلة.',
                        'وضع معايير وضوابط للبيانات التي يتم التعامل معها في مجالات حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية للوصول إلى نتائج علمية صحيحة ودقيقة.',
                        'تطوير وتدريب الباحثين والمهتمين بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، مع إعداد مواد تدريبية منهجية ونموذجية.',
                        'فتح قنوات التواصل مع التخصصات المختلفة من علمية وشرعية وأدبية وغيرها لخدمة حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، واستكشاف نقاط التقاطع بينها، وتحديد البحوث التقاطعية التي تخدمها.',
                        'تشجيع البحث العلمي في مجالات حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، وتوفير موضوعات بحثية وأفكار تطويرية وحلول تقنية للباحثين والمختصين في هذه المجالات.',
                        'نشر المعرفة والتوعية العامة بنتائج البحوث في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية بطريقة سهلة ومتاحة.',
                        'تشجيع الباحثين والمؤسسات المعنية بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية على المضي قدماً في إنتاجاتهم العلمية والإلكترونية بالبرمجيات مفتوحة المصدر.'
                    ]
                },
                'institute': {
                    'mission': {
                        'title': 'الرسالة',
                        'content': 'إنشاء وتطوير مرجعية علمية راسخة لحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، وتطوير البحوث والدراسات العلمية المتخصصة والبرامج الحاسوبية والمواقع الإلكترونية في هذا المجال، من خلال عمل مؤسسي متميز ومستدام، وبالتعاون والتنسيق مع المؤسسات والأفراد المتخصصين في المجالات الحاسوبية والشرعية واللغوية؛ مما يحقق رؤية متكاملة ومخرجات متميزة.'
                    },
                    'vision': {
                        'title': 'الرؤية',
                        'content': 'قيادة عالمية ومرجعية في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية'
                    },
                    'board': {
                        'title': 'مجلس الإدارة',
                        'members': [
                            {'name': 'أ.د. محمد زكي خضر', 'position': 'الرئيس'},
                            {'name': 'م. محمد محمد خير', 'position': 'المدير التنفيذي'},
                            {'name': 'د. مجدي صوالحة', 'position': 'مدير التقنية'},
                            {'name': 'أ.د. أكرم زكي', 'position': 'مدير المعلومات'},
                            {'name': 'د. مصطفى بوزريدة', 'position': 'مدير العمليات/السكرتير'},
                            {'name': 'م. محمد محمد خير', 'position': 'المدير المالي/أمين الصندوق'},
                            {'name': 'د. مجدي صوالحة', 'position': 'نائب الرئيس للخدمات التعليمية'},
                            {'name': 'أ. د. ياسر طرشاني', 'position': 'مدير'},
                            {'name': 'د. محمد شرف الدين مفتاح', 'position': 'مدير'},
                            {'name': 'د. محمد حميد الطائي', 'position': 'مدير'}
                        ]
                    },
                    'bylaws': {
                        'title': 'اللوائح',
                        'content': 'يعمل المعهد وفقاً للوائح شاملة تحكم أنشطته وعضويته وهيكله التنظيمي. تضمن هذه اللوائح الشفافية والمساءلة والالتزام بالمبادئ الإسلامية في جميع عملياتنا.'
                    },
                    'policy': {
                        'title': 'السياسات',
                        'content': 'تم تصميم سياساتنا للحفاظ على أعلى معايير النزاهة الأكاديمية وأخلاقيات البحث والقيم الإسلامية. نحن ملتزمون بتعزيز بيئة شاملة تعزز التميز في الدراسات الإسلامية الحاسوبية.'
                    },
                    'documents': {
                        'title': 'الوثائق الرسمية',
                        'bylaws_section': {
                            'title': 'نظام المعهد الأساسي',
                            'links': [
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_Arabic_نظام الدستور للمعهد',
                                    'url': 'https://drive.google.com/file/d/1UX8VZCOuvGGQnguGKIcKqVWf1Qe9nf35/view?usp=drive_link'
                                },
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_English',
                                    'url': 'https://drive.google.com/file/d/1Tt3RCHs8H0d1C54pLo2QkXDMLCL0xUnT/view?usp=drive_link'
                                },
                                {
                                    'title': 'Institute_nonprofit_bylaws_v3_French',
                                    'url': 'https://drive.google.com/file/d/16ORKC72Ia4IBRwVNDJbTRSIYFhZIRpss/view?usp=drive_link'
                                }
                            ]
                        },
                        'policies_section': {
                            'title': 'سياسات تضارب المصالح',
                            'links': [
                                {
                                    'title': 'Conflict Of Interest Policy v1 - Arabic',
                                    'url': 'https://drive.google.com/file/d/1A57AnKooMyzD7NNY0HkRWkyP25prpv9Y/view?usp=sharing'
                                },
                                {
                                    'title': 'Conflict Of Interest Policy v1 - English',
                                    'url': 'https://drive.google.com/file/d/1FgT-2X7c5PKkR_BlgOKuRZxoFAj1CeIA/view?usp=drive_link'
                                },
                                {
                                    'title': 'Conflict Of Interest Policy v1 - French',
                                    'url': 'https://drive.google.com/file/d/1hfk_mjOKDslQTJkNoES236rfpoA4lq6a/view?usp=drive_link'
                                }
                            ]
                        },
                        'profile_section': {
                            'title': 'الملف التعريفي للمعهد',
                            'links': [
                                {
                                    'title': 'الملف التعريفي v1',
                                    'url': 'https://drive.google.com/file/d/12PwULyGOLJ_ih3N4z5uatrpRJiMMmTRK/view?usp=drive_link'
                                }
                            ]
                        }
                    }
                },
                'activities': {
                    'title': 'الأنشطة والإهتمامات',
                    'sections': [
                        {
                            'title': 'توفر الموارد',
                            'content': 'يسعى المعهد إلى توفير المساحة والأدوات التي تسهل وتدعم وتدمج جهود الباحثين في خطط البحث المقترحة. قد تكون الموارد ممثلة بأجهزة الكمبيوتر أو خوادم قواعد البيانات التي تحتوي على تمثيل مفهرس ودقيق وموثق لنصوص القرآن الكريم بشكل خاص والمصادر الإسلامية بشكل عام، مع إضافة أدوات أو حزم للأغراض العامة لتحليل البيانات. يمكن أن توفر الموارد في سحابة مشتركة لاستضافة الأنظمة المختلفة التي ينشئها الباحثون في المجال.'
                        },
                        {
                            'title': 'تنظيم المؤتمرات وورش العمل والاجتماعات',
                            'content': 'يسعى المعهد إلى عقد مؤتمرات وورش عمل في مجال البحث التي تقع ضمن اهتمامات المعهد، إقليمياً ودولياً، شخصياً وإلكترونياً. كما يهدف المعهد إلى أن يكون المحرك لعقد اجتماعات بين الباحثين المهتمين بالبحث في نفس الموضوع، من خلال الاجتماعات عبر الإنترنت.'
                        },
                        {
                            'title': 'المنشورات',
                            'content': 'مع النمو المتوقع للمجتمع المهتم بخطط البحث المقترحة، ستكون هناك حاجة لتوفير وسائل النشر من المجلات العلمية وطرق نشر المعرفة اللازمة لتوفير بيئة مناسبة للبحث العلمي. كما يسعى المعهد إلى توفير منشورات عالية الجودة ودقيقة بعد المراجعة والتدقيق.'
                        },
                        {
                            'title': 'الدعم المالي والتبرعات',
                            'content': 'يعلن المعهد عن خطط عمله من أجل توفير الموارد المالية للمساهمة في دعم الباحثين والطلاب في أبحاثهم، وبناء المنصات العلمية وتوفير الأجهزة والبرمجيات والموارد السحابية اللازمة لاستضافة الأنظمة المختلفة من الحزم البرمجية العلمية والتقنية والخدمات الأخرى. لذلك، يقبل المعهد التبرعات المالية والعينية التي تخدم أهدافه بشكل عام أو لمشروع محدد ويراقب صرف الأموال بدقة وشفافية ضمن الضوابط المنصوص عليها في لوائح تأسيس المعهد.'
                        },
                        {
                            'title': 'الأنشطة الاستثمارية',
                            'content': 'قد يقوم المعهد بنشاط استثماري في المعاملات الإلكترونية أو غيرها لغرض الدعم المالي لنشاط المعهد، شريطة ألا يتجاوز ذلك نسبة الحدود المنصوص عليها في وثائق تأسيس المعهد ووفقاً للمعاملات الإسلامية المسموحة في الشريعة الإسلامية.'
                        },
                        {
                            'title': 'الشراكات التجارية والتطبيقات',
                            'content': 'نظراً لأن البيانات والمعلومات والبرمجيات المتعلقة بنشاط المعهد يمكن أن تأخذ طريقها إلى التطبيق العملي من خلال الشركات والمؤسسات التجارية أو المهنية أو العلمية؛ سيكون المعهد منفتحاً للتعاقد والتعاون والمشاركة في التطبيقات الإلكترونية، سواء كانت تعليمية أو خدمية متعلقة بمصالح المعهد، مثل الشركات والمؤسسات، ضمن ضوابط يتم دراستها بطريقة لا تتعارض مع وثائق تأسيس المعهد.'
                        },
                        {
                            'title': 'البرمجيات مفتوحة المصدر',
                            'content': 'يسعى المعهد إلى أن تكون البرمجيات التي يعمل عليها مفتوحة المصدر قدر الإمكان، بهدف تطوير عمله وتشجيع التعاون والمشاركة في تقدم البشرية، دون أي نوع من الاحتكار من قبل شركات ومؤسسات معينة، واعتبار مثل هذا النشاط أفضل مقارنة بالبرمجيات غير مفتوحة المصدر.'
                        },
                        {
                            'title': 'إدارة الأوقاف الإلكترونية',
                            'content': 'يقبل المعهد نيابة عن الأفراد والمؤسسات والجمعيات التي تراقب الأوقاف، حيث يديرها وفقاً لشروط الواقفين، والتي تكون في خدمة حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية. في وثائق الوقف، وبطريقة لا تتعارض مع النظام الأساسي للمعهد.'
                        },
                        {
                            'title': 'الدعم المهني والتطوير',
                            'content': 'يهدف المعهد إلى دعم طلاب البكالوريوس والدراسات العليا المهتمين بخطط البحث المقترحة وتسهيل فرص المنح الدراسية الممكنة. علاوة على ذلك، يلتزم المعهد بالسعي لتطوير قدرات أعضاء هيئة التدريس والباحثين والمهنيين العاملين مع تقدمهم في حياتهم المهنية. يدعم المعهد عملية ترقية خطط البحث المقترحة كمسار وظيفي وطريق للنجاح في الحياة الأكاديمية والمهنية، وبناء منصة علمية للتدريب وتوفير الحلول والخبرة التقنية المتخصصة لجميع الباحثين والعلماء.'
                        },
                        {
                            'title': 'الدرجات الأكاديمية والبرامج',
                            'content': 'في السنوات القادمة، يسعى المعهد إلى تطوير برامج أكاديمية لمستويات البكالوريوس والماجستير والدكتوراه، متخصصة في حوسبة القرآن الكريم والعلوم الإسلامية. كما يسعى إلى اعتماد هذه البرامج الأكاديمية من المؤسسات الدولية التي تمنح الاعتماد الدولي للبرامج الأكاديمية مثل ABET في الهندسة وعلوم الكمبيوتر وغيرها.'
                        }
                    ]
                },
                'training': {
                    'title': 'برامج التدريب',
                    'description': 'يقدم المعهد برامج تدريبية شاملة مصممة لسد الفجوة بين التكنولوجيا والعلوم الإسلامية.',
                    'courses': [
                        {
                            'title': 'مقدمة في العلوم الإسلامية واللغوية للمختصين التقنيين',
                            'description': 'هذه الدورة مصممة للمختصين التقنيين الذين يريدون فهم العلوم الإسلامية واللغوية. توفر المعرفة الأساسية اللازمة لتطوير التطبيقات الحاسوبية في الدراسات الإسلامية، وتغطي المفاهيم الأساسية في الفقه الإسلامي واللسانيات العربية والدراسات القرآنية.'
                        },
                        {
                            'title': 'دورة تقنية المعلومات في خدمة العلوم الإسلامية',
                            'description': 'تركز هذه الدورة الشاملة على تطبيق تقنية المعلومات الحديثة لخدمة العلوم الإسلامية. سيتعلم المشاركون عن تصميم قواعد البيانات للنصوص الإسلامية، ومعالجة اللغة الطبيعية للعربية، والحفظ الرقمي للمخطوطات الإسلامية، وتطوير البرمجيات التعليمية الإسلامية.'
                        }
                    ]
                },
                'projects': {
                    'title': 'المشاريع البحثية',
                    'content': 'يشارك معهدنا في مشاريع بحثية متطورة مختلفة تجمع بين الطرق الحاسوبية والدراسات الإسلامية. تشمل هذه المشاريع أدوات تحليل القرآن الرقمية، ورقمنة المخطوطات الإسلامية، ومعالجة اللغة الطبيعية العربية، والبرمجيات التعليمية للدراسات الإسلامية. نتعاون مع المؤسسات الدولية لتطوير المجال وتوفير أدوات قيمة للباحثين والعلماء في جميع أنحاء العالم.'
                },
                'news': {
                    'title': 'آخر الأخبار',
                    'content': 'ابق على اطلاع بآخر التطورات والإعلانات والإنجازات من المعهد العالمي لحوسبة القرآن والعلوم الإسلامية. ننشر بانتظام تحديثات حول تقدم أبحاثنا والمؤتمرات القادمة وبرامج التدريب والمبادرات التعاونية.',
                    'links': [
                        {
                            'title': 'أنشطة المعهد',
                            'url': 'https://drive.google.com/file/d/19LGkjPZJDAQLQVDP47ns_aFca-YBaKuI/view?usp=sharing'
                        },
                        {
                            'title': 'الإجتماع السنوي الثاني - المعهد العالمي لحوسبة القرآن والعلوم الإسلامية -2024-05-25 (B)',
                            'url': 'https://drive.google.com/file/d/1XBxblr8iVJSUIbkh4BL-U17wueTBXKfk/view?usp=drive_link'
                        },
                        {
                            'title': 'قناة الفيديو على يوتيوب',
                            'url': 'https://www.youtube.com/@qurancomputing7916',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png'
                        },
                        {
                            'title': 'إكس (تويتر)',
                            'url': 'https://twitter.com/QuranComputing',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg'
                        },
                        {
                            'title': 'فيسبوك',
                            'url': 'https://www.facebook.com/QuranComputing/',
                            'icon': 'https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg'
                        }
                    ]
                },
                'members': {
                    'title': 'الأعضاء',
                    'content': 'يجمع معهدنا مجتمعاً متنوعاً من الباحثين والعلماء والمهنيين من جميع أنحاء العالم. يشمل أعضاؤنا علماء الكمبيوتر والعلماء الإسلاميين واللغويين والمربين الذين يتشاركون هدفاً مشتركاً في تطوير الدراسات الإسلامية الحاسوبية.'
                },
                'contact': {
                    'title': 'اتصل بنا',
                    'email': 'info@qurancomputing.org',
                    'content': 'نرحب بالاستفسارات والتعاون والاقتراحات. لا تتردد في الاتصال بنا لأي أسئلة أو فرص للشراكة. فريقنا مستعد دائماً لمساعدة الباحثين والطلاب والمؤسسات المهتمة بالدراسات الإسلامية الحاسوبية.'
                },
                'donations': {
                    'title': 'التبرعات',
                    'content': 'المعهد العالمي لحوسبة القرآن والعلوم الإسلامية مؤسسة غير ربحية في الولايات المتحدة الأمريكية معفية من الضرائب 88-1219520. للحوالة المالية بشكل مباشر تواصل معنا info@qurancomputing.org',
                    'donation_links': [
                        {
                            'title': 'فيزا أو ماستركارد',
                            'url': 'https://donate.stripe.com/dR616G9Uk7C78WA5kk'
                        },
                        {
                            'title': 'باي بال',
                            'url': 'https://www.paypal.me/qurancomputing'
                        }
                    ]
                }
            }
        }
    
    def get_content(self, section, language='ar', subsection=None):
        """Get content for a specific section and language"""
        try:
            if subsection:
                return self.content[language][section][subsection]
            return self.content[language][section]
        except KeyError:
            return {'title': 'Content Coming Soon', 'content': 'Information will be available soon.'}
    
    def get_all_content(self, language):
        """Get all content for a specific language"""
        return self.content.get(language, {})

