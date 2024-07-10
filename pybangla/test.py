import time
from module.main import Normalizer

if __name__ == "__main__":


    # # Testing Date format
    # date_list = [
    #     "০১-এপ্রিল/২০২৩",
    #     "সেপ্টেম্বর ০৫ ২০২৩",
        # "01-Apr/2023"
        # "এপ্রিল ২০২৩" 
        # "2023-04-05",  
        # "06-04-2023", 
        # "04/01/2023",  
        # "07 April, 2023", 
        # "Apr 1, 2023",  
        # "2023/04/01", 
        # "01-Apr-2023", 
        # "01-Apr/2023",  
        # "20230401",  
        # "20042024",
        # "20230401",
        # ["1", "4", "2025"]
    # ]
    # # # # number = "123456" or "২০২৩"
    # # number = "২০২৩"
    nrml = Normalizer()
    # # # # # print("++++++++++++++++++++ Date testing ++++++++++++++++++++++")
    # # # # print("Date format Testing : ", end ="", flush=True)
    # for date_ in date_list:
    #     start_time = time.time()
    #     print("date_:", date_)
    #     formated_date = nrml.date_format(date_, language="en")
    #     print(formated_date)
    # # print("++++++++++++++++++++ end of Date testing ++++++++++++++++++++++")

    # # print("++++++++++++++++++++ en number to bn number convert ++++++++++++++++++++++")
    # number = "1234"
    # number = nrml.number_convert(number, language="en")
    
    
    # number = nrml.number_convert(number, language="bn")

    # print("Bn Number : ", number)
    # print("++++++++++++++++++++ stop number convert ++++++++++++++++++++++")

    # # print("++++++++++++++++ Today +++++++++++++++++++++")
    # today_date = nrml.today(language="bn")
    # # today_date = nrml.today(language="en")
    # print(today_date)

    # # print("++++++++++++++++ End Today +++++++++++++++++++++")
    # # # print(today_date)
    # # print("++++++++++++++++ weekdays +++++++++++++++++++++")
    # weekdays = nrml.weekdays()
    # weekdays = nrml.weekdays(language="bn")
    # weekdays = nrml.weekdays(language="en")
    # weekdays = nrml.weekdays(day = "সোমবার")
    # weekdays = nrml.weekdays(day = "Monday")
    # print(weekdays)

    # # print("++++++++++++++++ end weekdays +++++++++++++++++++++")
    # # # print(weekdays)
    # # print("+++++++++++++++ seasons ++++++++++++++++++++++++")
    # seasons = nrml.seasons()
    # seasons = nrml.seasons(language="bn")
    # seasons = nrml.seasons(language="en")
    # seasons = nrml.seasons(seasons = "গ্রীষ্ম")
    # print(seasons)

    # # print("+++++++++++++++ end seasons ++++++++++++++++++++++++")

    # # print("+++++++++++++++++ months +++++++++++++++++++++++++++")
    # month = nrml.months()
    # month = nrml.months(month="মার্চ")
    # print(month)


    # text = "রাহিম ক্লাস ওয়ান এ ১ম, ১১তম ২২ তম ৩৩ তম, ১২৩৪ শতাব্দীতে ¥২০৩০.১২৩৪ বিবিধ  বাকেরগঞ্জ উপজেলার প্রায় 40 ভাগের পেশাই চাষাবাদ 80 and 40 ২২"
    
    # text = nrml.text_normalizer(text)

    # print(text)

    # input_texts = [
    #     "আমি এক দুই তিন চার পাঁচ টু থ্রি ফাইভ ছয় সেভেন এইট নাইন শূন্য আমার ফোন নাম্বার জিরো ওয়ান ডাবল সেভেন",
    #     "ওয়ান ডাবল নাইন টু",
    #     "একশ বিশ টাকা",
    #     "জিরো টু ডাবল ওয়ান",
    #     "জিরো ওয়ান ডাবল সেভেন থ্রি ডাবল ফাইভ নাইন থ্রি সেভেন নাইন",
    #     "আমার ফোন নম্বর জিরো ওয়ান ডাবল সেভেন থ্রি ডাবল ফাইভ নাইন থ্রি সেভেন নাইন",
    #     "ট্রিপল টু ওয়ান",
    #     "দুই হাজার চারশো বিশ",
    #     "দুই হাজার চারশ  বিশ",
    #     "হাজার বিশ",
    #     "ডাবল নাইন টু",
    #     "এক লক্ষ চার হাজার দুইশ",
    #     "এক লক্ষ চার হাজার দুইশ এক",
    #     "এক লক্ষ চার হাজার দুইশ এক টাকা এক দুই",
    #     "আমাকে এক লক্ষ দুই হাজার টাকা দেয়",
    #     "আমাকে এক লক্ষ দুই হাজার এক টাকা দেয় এন্ড তুমি বিশ হাজার টাকা নিও এন্ড এক লক্ষ চার হাজার দুইশ এক টাকা এক ডবল দুই",
    #     "ছয় হাজার বিশ",
    #     "আমার সাড়ে পাঁচ হাজার",
    #     "আমার সাড়ে তিনশ",
    #     "আড়াই হাজার",
    #     "আড়াই লক্ষ",
    #     "ডেরশ",
    #     "আমাকে ডেরশ টাকা দেয়",
    #     "সাড়ে পাঁচ কোটি টাকা",
    #     "সাড়ে 1254 টাকা",
    #     "জিরো",
    #     "একশ বিশ take একশ",
    #     "জিরো টু ডাবল ওয়ান",
    #     "জিরো টু ওয়ান ওয়ান",
    #     "থ্রি ফোর ফাইভ এইট",
    #     "একশ বিশ টাকা",
    #     "ডাবল ওয়ান ডবল টু",
    #     "জিরো ওয়ান টু",
    #     "থ্রি ফোর ফাইভ সিক্স",
    #     "সেভেন এইট নাইন টেন",
    #     "একশ দুইশ তিনশ",
    #     "চারশ পাঁচশ",
    #     "ছয়শ সাতশ",
    #     "আটশ নয়শ",
    #     "দশ তিরানব্বই",
    #     "ট্রিপল থ্রি টু",
    #     "শূন্য এক দুই তিন",
    #     "চার পাঁচ ছয় সাত",
    #     "আট নয় দশ এগারো",
    #     "বারো তেরো চৌদ্দ পনেরো",
    #     "ষোল সতেরো আঠারো উনিশ",
    #     "বিশ একুশ বাইশ তেইশ",
    #     "চব্বিশ পঁচিশ ছাব্বিশ সাতাশ",
    #     "আঠাশ ঊনত্রিশ ত্রিশ একত্রিশ",
    #     "বত্রিশ তেত্রিশ চৌত্রিশ পঁয়ত্রিশ",
    #     "ছত্রিশ সাঁইত্রিশ আটত্রিশ ঊনচল্লিশ",
    #     "চল্লিশ একচল্লিশ বিয়াল্লিশ তেতাল্লিশ",
    #     "চুয়াল্লিশ পঁয়তাল্লিশ ছেচল্লিশ সাতচল্লিশ",
    #     "আটচল্লিশ ঊনপঞ্চাশ পঞ্চাশ একান্ন",
    #     "বাহান্ন তিপ্পান্ন চুয়ান্ন পঞ্চান্ন",
    #     "ছাপ্পান্ন সাতান্ন আটান্ন ঊনষাট",
    #     "ষাট একষট্টি বাষট্টি তেষট্টি",
    #     "চৌষট্টি পঁয়ষট্টি ছেষট্টি সাতষট্টি",
    #     "আটষট্টি ঊনসত্তর সত্তর একাত্তর",
    #     "বাহাত্তর তিয়াত্তর চুয়াত্তর পঁচাত্তর",
    #     "ছিয়াত্তর সাতাত্তর আটাত্তর ঊনআশি",
    #     "আশি একাশি বিরাশি তিরাশি",
    #     "চুরাশি পঁচাশি ছিয়াশি সাতাশি",
    #     "আটাশি ঊননব্বই নব্বই একানব্বই",
    #     "বিরানব্বই তিরানব্বই চুরানব্বই পঁচানব্বই",
    #     "ছিয়ানব্বই সাতানব্বই আটানব্বই নিরানব্বই",
    #     "এক লক্ষ চার হাজার দুইশ এক টাকা এক দুই",
    #     "তিনশ পঁচিশ পাঁচশ",
    #     "তিনশ পঁচিশ পাঁচশ এক",
    #     "চা-পুন",
    #     "ওকে",
    #     "ডের আউটস্ট্যান্ডিং কত",
    #     "ডাবল",
    #     "নাইন ডাবল এইট",
    #     "দশ বারো এ এগুলা একশ একশ দুই",
    #     "এক লক্ষ তেত্রিশ চার",
    #     "আমাকে এক লক্ষ দুই হাজার এক টাকা দেয় এন্ড তুমি বিশ হাজার টাকা নিও এন্ড এক লক্ষ চার হাজার দুইশ এক টাকা এক ডবল দুই"
    #     ]
    # for i in input_texts:
    #     print("="*40)
    #     print("input : ", i)
    #     text = nrml.word2number(i)
    #     print("output : ", text)
    #     print("="*40)
    # text = "সম্মেলনটি সেপ্টেম্বর ০৫ ২০২৩ তারিখে নির্ধারিত করা হয়েছে. এপ্রিল ২,০২৩"
    # formated_date = nrml.date_extraction(text)

    # print(formated_date)

    # # text = "৫ বছরে নন-ক্যাডার পদে ৭,৪৪৭ জনকে নিয়োগের সুপারিশ করা হয়েছে 1,230"
    # text = "৫ বছরে নন-ক্যাডার পদে ৭,৪৪৭ জনকে নিয়োগের সুপারিশ করা হয়েছে"

    # text = "শীঘ্রই ভিক্টোরিয়ার এক প্রতিনিধিদল আসছেন,শিলংয়ের ব্রুকসাইড হাউসে"

    # text = "The numbers are 10 নন-ক্যাডার 20.5  30, and 40.75. সুপারিশ ২০৩০.৩০ 12 23 45"

    # bangla_sentences = [
    # "১৯৯৬ সালের ৬ তারিখে নির্ধারিত করা হয়েছে.",
    # "১৯৯৬ সালের ৬ সেপ্টেম্বর ভ্রমণ পরিকল্পনা করছি.",
    # "আমি জুলাই ২০২৩ তে একটি সমুদ্র ভ্রমণ পরিকল্পনা করছি.",
    # "সম্মেলনটি সেপ্টেম্বর ০৫ ২০২৩ তারিখে নির্ধারিত করা হয়েছে.",
    # "আমরা খ্রীষ্টমাসের জন্য ডিসেম্বর ২৫ ২০২৩ তারিখে পরিবারের সংগঠন করব.",
    # "আমার বোনের বিয়ে ১৮ মার্চ, ২০২৩ তারিখে.",
    # "আমি আগামী ১২ আগস্ট, ২০২৩ তারিখে আমার জন্মদিনে দেখা করছি.",
    # "আমরা ফেব্রুয়ারি ২০২৩ তে স্কিউইং যাব.",
    # "আমাদের কোম্পানির পিকনিকটি জুন ৩০ ২০২৩ তারিখে নির্ধারিত হয়েছে.",
    # "আমার গুরুত্বপূর্ণ পরীক্ষা ১০ মে, ২০২৩ তারিখে.",
    # "নতুন সেমিস্টার শুরু হয় জানুয়ারি ২০২৩ তারিখে.",
    # "আমরা এপ্রিল ২০২৩ তে একটি রোড ট্রিপ পরিকল্পনা করছি.",
    # "আমি অক্টোবর ২০২৩ তারিখে একটি নতুন অ্যাপার্টমেন্টে যাচ্ছি.",
    # "আপনার ক্যালেন্ডারের মার্ক নভেম্বর ০৫, ২০২৩, এটি দীপাবলি.",
    # "আমি জুলাই ২০২৩ তারিখে গরম শিবিরের জন্য উৎসাহিত.",
    # "মার্চ ২৫, ২০২৩ তারিখের কনসার্ট টিকেটগুলি দ্রুত বিক্রয় হচ্ছে.",
    # "আগস্ট ২০২৩ তারিখে একটি বারবিকিউ পার্টি আয়োজন করা হবে.",
    # "আমি মে ২০২৩ তারিখে আমার নানা-নানির কাছে যাচ্ছি.",
    # "আমি সেপ্টেম্বর ২০২৩ তারিখে একটি বিয়ে অনুষ্ঠানে যাচ্ছি.",
    # "আমরা জুন ২০২৩ তে ইউরোপে একটি ভ্রমণ পরিকল্পনা করছি.",
    # "আমার ডেন্টিস্টের অ্যাপয়েন্টমেন্ট এপ্রিল ১০, ২০২৩ তারিখে.",
    # "কোম্পানির বার্ষিক সভা ফেব্রুয়ারি ২০২৩ তারিখে হয়.",
    # "আমার অনুষ্ঠান সমাপন হয়েছে জুন ১৫, ২০২৩ তারিখে.",
    # "আমি মার্চ ২০২৩ তারিখে একটি নতুন চাকরি শুরু করছি.",
    # "আমি মে ২০২৩ তারিখে পাহাড়ে ট্রেকিং করতে যাচ্ছি.",
    # "বিদ্যালয়ের নাটকটি নভেম্বর ২০২৩ তারিখে নির্ধারিত হয়েছে.",
    # "আমরা অক্টোবর ২০২৩ তার",
    # "১৯৯৬ সালের ৬ সেপ্টেম্বর",
    # "২০৩০ সালের ৬ সেপ্টেম্বর",
    # "১৯৯৬ সালের৬ তারিখে নির্ধারিত করা হয়েছে.",
    # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা করছি ২০৩০সালের ৬সেপ্টেম্বর",
    # "এয়ারলাইনসসহ তিনটি এয়ারলাইনসের ৫১টি ফ্লাইটে মো: ২০ হাজার ২৯১ জন হজযাত্রী সৌদি আরবে গেছেন। এ বছর হজ করতে ৮৫ হাজার ২৫৭ জনের সৌদি আরবে যাওয়ার কথা রয়েছে।",
    # " সাঃ কিমি হাফিক বিডিটি এয়ারলাইনসসহ তিনটি এয়ারলাইনসের ৫১টি কিমি. ফ্লাইটে মোট ২০ হাজার ২৯১ জন হজযাত্রী সৌদি আরবে গেছেন। এ বছর হজ করতে ৮৫ হাজার ২৫৭ জনের সৌদি আরবে যাওয়ার কথা রয়েছে। ৫ম",
    # "প্রদর্শনীটি চলার কথা ছিল ১২ মে পর্যন্ত, তবে দর্শকদের ব্যাপক আগ্রহের কারণে তিন দিন সময় বাড়িয়ে ১৫ মে পর্যন্ত করা হয়েছিল ১৫.১৫",
    # "The numbers are 10 নন-ক্যাডার 20.5  30, and 40.75. সুপারিশ ২০৩০.৩০ 12 23 45",
    # "[১৯৯৬]-সালের-৬:তারিখে-নির্ধারিত করা হয়েছে"
    # ]

    # # solving steps is have number need to give extra space both side
    # issue = [
    # # "[১৯৯৬]-সালের-৬:তারিখে-নির্ধারিত করা হয়েছে.",
    # # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা করছি ২০৩০সালের ৬সেপ্টেম্বর",
    # # "আজকের তাপমাত্রা ৪৪°F",
    # # "আজকের তাপমাত্রা ৪৪°C",
    # # "যেমন ১৯৬১ সালে দেশটির তৎকালীন প্রেসিডেন্ট ডোয়াইট ডি আইজেনহাওয়ার শিক্ষা খাতে সামরিক শিল্পের প্রবেশের বিপদ নিয়ে সতর্ক করেছিলেন।",
    # # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা করছি ২০৩০সালের ৬সেপ্টেম্বর",
    # "উদাহরণস্বরূপ, আপনার মোটরযানের রেজিস্ট্রেশন নাম্বার ঢাকা মেট্রো-গ-12-1212 এবং টাকা জমা রশিদের ট্রানজেকশন নাম্বার 2001011325989"
    # ]

    issue = [
    # "[১৯৯৬]-সালের-৬:তারিখে-নির্ধারিত করা হয়েছে. ১৯৯৬-৯৬",
    # "১৯৮৭-র ১৯৯৫ সালে",
    # "দয়া !@করে #পবিত্র &)কুরআনুল *কারিম বলেন,,,,পবিত্র কথাটা অবশ্যই বলবেন,,, প্লিজ",
    # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা ৬ সেপ্টেম্বর করছি ২০৩০সালের ২সেপ্টেম্বর",
    # " দুর্নীতির মাধ্যমে অর্জিত আয়ের উৎস গোপনের জন্য নিজের নামসহ তাঁর আত্মীয়স্বজনের নামে ৭০০০টির বেশি হিসাব খোলেন।"
    # "১৯৯৬ সালের নির্ধারিত করা হয়েছে. ১৯৯৬-৯৬",
    # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা করছি ২০৩০সালের ৬সেপ্টেম্বর দুর্নীতির মাধ্যমে অর্জিত আয়ের উৎস গোপনের জন্য নিজের নামসহ তাঁর আত্মীয়স্বজনের নামে ৭০০০টির বেশি হিসাব খোলেন।",
    # "আজকের তাপমাত্রা৪৪°F",
    # "আজকের তাপমাত্রা ৪৪°C",
    # "যেমন ১৯৬১ সালে দেশটির তৎকালীন প্রেসিডেন্ট ডোয়াইট ডি আইজেনহাওয়ার শিক্ষা খাতে সামরিক শিল্পের প্রবেশের বিপদ নিয়ে সতর্ক করেছিলেন।",
    # "১৯৯৬সালের ৬ সেপ্টেম্বররণ ভ্রমণ পরিকল্পনা করছি ২০৩০সালের ৬সেপ্টেম্বর",
    # " বাংলাদেশের পাসপোর্টের অভ্যন্তরে ইস্যু করানোর সময়ে নিয়মিত, জরুরী, এবং অতীব জরুরী বিতরণের ফি নিম্নলিখিত: নিয়মিত বিতরণ (48 পৃষ্ঠা এবং 10 বছর মেয়াদ) পাসপোর্ট ফি: ৪,০২৫ টাকা জরুরী বিতরণ (48 পৃষ্ঠা এবং 10 বছর মেয়াদ) পাসপোর্ট ফি: ৬,৩২৫ টাকা অতীব জরুরী বিতরণ (48 পৃষ্ঠা এবং 10 বছর মেয়াদ) পাসপোর্ট ফি: ৮,৬২৫ টাকা নিয়মিত বিতরণ (64 পৃষ্ঠা এবং 5 বছর মেয়াদ) পাসপোর্ট ফি: ৫,৭৫০ টাকা জরুরী বিতরণ (64 পৃষ্ঠা এবং 5 বছর মেয়াদ) পাসপোর্ট ফি: ৮,০৫০ টাকা অতীব জরুরী বিতরণ (64 পৃষ্ঠা এবং 5 বছর মেয়াদ) পাসপোর্ট ফি: ১০,৩৫০ টাকা",
    # "বাংলাদেশের পাসপোর্টের অভ্যন্তরে ইস্যু করানোর সময় 10/12/1956",
    # "৬/৯/১৯৯৬ বাংলাদেশের পাসপোর্টের অভ্যন্তরে ইস্যু করানোর সময় 10/12/24",
    # "ডিজিটাল রেজিস্ট্রেশন সার্টিফিকেট সংক্রান্ত যোগাযোগ করতে হলে 01790-111111 অথবা 01790-540210 নম্বরে যোগাযোগ করতে হবে +8801790540211",
    # "ডিজিটাল রেজিস্ট্রেশন সার্টিফিকেট সংক্রান্ত যোগাযোগ করতে হলে ০১৭৯০-১১১১১১ অথবা ০১৭৯০-৫৪০২১০ নম্বরে যোগাযোগ করতে হবে ০১৭৯০৫৪০২১১",
    # "রাহিম ক্লাস ওয়ান এ ১ম, ১১তম ২২ তম ৩৩ তম, ১২৩৪ শতাব্দীতে ¥২০৩০.১২৩৪ বিবিধ  বাকেরগঞ্জ উপজেলার প্রায় 40 ভাগের পেশাই চাষাবাদ 80 and 40 ২২"
    # "অর্থাৎ, আবেদনকারীর বয়স ১ বছর হলে জন্ম নিবন্ধন ফি ১০ টাকা, বয়স ২ বছর হলে ২০ টাকা, বয়স ৫ বছর হলে ৫০ টাকা, এবং বয়স ১০ বছর হলে ১০০ টাকা হবে",
    # "বাংলাদেশের পাসপোর্টের ৪৮ পৃষ্ঠা এবং ১০ বছর মেয়াদের সহ পাসপোর্টের জন্য নিয়মিত বিতরণে ফি ৫,৭৫০ টাকা, জরুরী বিতরণে ফি ৮,০৫০ টাকা, এবং অতীব জরুরী বিতরণের ফি ১০,৩৫০ টাকা",
    # "১৯৯৬ টাকা বাংলাদেশের পাসপোর্টের ৬৪ পৃষ্ঠা এবং ৫ বছর মেয়াদের সহ পাসপোর্টের জন্য নিয়মিত বিতরণে ফি ৬,৩২৫ টাকা, জরুরী বিতরণে ফি ৮,৬২৫.৬২৫ টাকা, এবং অতীব জরুরী বিতরণের ফি ১২,০৭৫ টাকা"
    "১৯৫৪ সাল। কালো রাত।"
    ]



    for i in issue:

        print("input : ", i)
        text = nrml.text_normalizer(i)
        print("output : ", text)

        print("="*2)
        print(nrml.text_diff(i, text))
        # print()
        print("+"*40)

    # number_string = nrml.process_phone_number("01790-540211")
    # print(number_string)

