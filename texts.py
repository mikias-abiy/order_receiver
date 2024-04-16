#!/usr/bin/python3


AM = {
    'start_keys': ['ዕቃዎች', 'ትዕዛዝ', 'የኔ ትዕዛዝ', 'ቋንቋ', 'ስለ መተግበሪያው'],
    'about': '''\
ትዕዛዝ ተቀባይ ቴሌግራም ቦት

 ይህ ቦት የተዘጋጀው በእቃዎች ክፍል ውስጥ የተዘረዘሩትን ዕቃዎች ትዕዛዝ ለመቀበል፣፣ ለማስተካከል፣ ለማጥፋት ነው።

 ለንግድዎ እንዲህ ያለ ቦት ከፈለጉ በዚህ አድራሻ ሊያገኙን ይችላሉ: @mikiasab
''',
    'items_caption': ['ስም', 'ዋጋ'],
    'order_prompots': {
            'orderer_name': 'የዓዛዥ ሙሉ ስም',
            'orderer_phone': [
                'የስልክ ቁጥርን ለማጋራት ከታች ያለውን ቁልፍ ይጫኑ', 'ስልክ ቁትርዎን ያጋሩ'
                ],
            'orderer_address': 'ዕቃው የደሚደርስበትን አድራሻ ያስገቡ',
            'item_name': 'የዕቃው ስም ይምረጡ',
            'item_color': 'የዕቃው ቀለም ይምረጡ',
            'item_amount': 'የዕቃው ብዛት (በአሐዝ)',
            'item_last': """ትዕዛዝ መጨመር ከፈልጉ 'ትዕዛዝ ጨምር ሚለውን' ይጫኑ።
ከጨረሱ ጨርሻለው ሚለውን ይጫኑ።\nማቋረጥ ከፈልጉ ያቋርጡ ሚልውን ይጫኑ።"""
        },
    'orders': [
            'ስም', 'ስልክ', 'አድራሻ', 'ትዕዛዞች'
        ],
    'colors': [
            "ጥቁር", "ወርቃማ", "መዳብ", "ፈዛዛ አረንጓዴ", "ክሬም",
            "ጥቁር በነጭ ደብዛዛ ዥንጉርጉር", "ጥቁር በነጭ ደማቅ ዥንጉርጉር",
            "አረንጓዴ በወርቃም ዥንጉርጉር", "ሰማያዊ በወርቃም ዥንጉርጉር",
        ],
    'cancle': 'ያቋርጡ',
    'done': 'ጨርሻለው',
    'add_order': 'ትዕዛዝ ጨምር',
    'order_success': '''\
ትዕዛዝዎ በተሳካ ሁኔታ ተመዝግቡኣል።
ትዕዛዝዎ ሲደርስ ደውለን እናሳውቆታለን።
ዓገልግሎቱን ስለተጠቀሙ እናመሰግናለን።''',
    'previous_order': '''\
ትዕዛዝዎን መቀየር ከፈለጉዎ ቀደም ሲል ያዘዙትን  "የኔ ትዕዛዝ" የሚለውን ቁልፍ ተጭነው እዚያ ማስተካከል ይችላሉ።
እናመሰግናለን።''',
    'no_previous_order': '''ይቅርታ ከዚህ በፊት ያዘዙት ትዕዛዝ የለም።'''
}


EN = {
    'start_keys': ['Items', 'Order', 'My Order', 'Language', 'About'],
    'about': """\
Order Receiver Telegram Bot

This bot was specifically designed to receive, take, edit, delete \
orders of items that are list in the items section.

If you want such bot for your business feel free to contact us here: @mikiasab
""",
    'items_caption': ['Name', 'Price'],
    'order_prompots': {
            'orderer_name': "Orderer's full name",
            'orderer_phone': [
                "Press the key below to share your contact", "Share contact"
                ],
            'orderer_address':
            "Enter the address to where the item(s) will be delivered",
            'item_name': "Choose the item's name",
            'item_color': "Choose the item's color",
            'item_amount': "Enter the item's amount (in numbers)",
            'item_last': """If you want to add more items press 'Add Order'.
If you are done press 'Done'.\nIf you want to cance press 'Cancle'."""
        },
    'orders': [
            'Name', 'Phone', 'Address', 'Orders'
        ],
    'colors': [
            "Black", "Golden", "Silver", "Light Green", "Creame",
            "Black in white fuzzy jerky", "Black in white bright jerky",
            "Green with golden jerky", "Blue with golden jerky"
        ],
    'cancle': "Cancle",
    'done': "Done",
    'add_order': 'Add order',
    'order_success': '''\
Your order has been registered successfuly.
We will call you once the orders are done.
Thankyou for using our service.''',
    'previous_order': '''\
You already have a previous order.
If you wanna update your order press "My Order" key and you can edit it there.
Thankyou.''',
    'no_previous_order': "Sorry you don't have any order"
}
