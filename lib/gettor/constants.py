#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
"""
 constants.py

 Copyright (c) 2008, Jacob Appelbaum <jacob@appelbaum.net>,
                     Christian Fromme <kaner@strace.org>

 This is Free Software. See LICENSE for license information.

"""

# Giant multi language help message. Add more translations as they become ready
multilanghelpmsg = """
    Hello! This is the "GetTor" robot.

    Unfortunately, we won't answer you at this address. You should make
    an account with GMAIL.COM or YAHOO.CN and send the mail from
    one of those.

    We only process requests from email services that support "DKIM",
    which is an email feature that lets us verify that the address in the
    "From" line is actually the one who sent the mail.

    (We apologize if you didn't ask for this mail. Since your email is from
    a service that doesn't use DKIM, we're sending a short explanation,
    and then we'll ignore this email address for the next day or so.)

    Please note that currently, we can't process HTML emails or base 64
    mails. You will need to send plain text.

    If you have any questions or it doesn't work, you can contact a
    human at this support email address: tor-assistants@torproject.org

    --

    �~Eرحبا! أ�~Fا ر�~Hب�~Hت "احص�~D ع�~D�~I ت�~Hر".

    �~D�~Dأس�~A �~D�~F �~Fرد ع�~D�~J�~C ع�~D�~I �~Gذا ا�~Dع�~F�~Hا�~F. �~Jت�~Hجب ع�~D�~J�~C أ�~F ت�~Fشئ
    حسابا�~K ع�~D�~I GMAIL.COM أ�~H YAHOO.COM �~Hترس�~D رسا�~Dة إ�~D�~Cتر�~H�~F�~Jة
    �~E�~F 
    أحد�~G�~Eا.

    �~F�~B�~H�~E ب�~Eعا�~Dجة ا�~Dط�~Dبات �~E�~F خد�~Eات ا�~Dبر�~Jد ا�~Dت�~J تدع�~E "DKIM"�~L
    �~H�~G�~J خاصة تس�~Eح �~D�~Fا با�~Dتح�~B�~B �~E�~F أ�~F ا�~Dع�~F�~Hا�~F �~A�~J
    ح�~B�~D ا�~D�~Eرس�~D �~G�~H با�~D�~Aع�~D �~E�~F �~Bا�~E بإرسا�~D ا�~Dرسا�~Dة.

    (�~Fعتذر إ�~F �~D�~E ت�~C�~F �~Bد ط�~Dبت �~Gذ�~G ا�~Dرسا�~Dة. ب�~Eا أ�~F بر�~Jد�~C �~E�~Bد�~E �~E�~F
    خد�~Eة �~Dاتستخد�~E KDIM�~L �~B�~E�~Fا بإرسا�~D شرح �~E�~Hجز�~L
    �~Hس�~Fتجا�~G�~D ع�~F�~Hا�~F ا�~Dبر�~Jد �~Gذا خ�~Dا�~D ا�~D�~J�~H�~E ا�~Dتا�~D�~J ت�~Bر�~Jبا�~K).

    �~Jرج�~I �~E�~Dاحظة أ�~F�~Fا �~Dا �~Fستط�~Jع �~Eعا�~Dجة رسائ�~D HTML أ�~H base 64
    . ستحتاج أ�~F ترس�~D �~D�~Fا رسا�~Dة تحت�~H�~J ع�~D�~I �~Fص بس�~Jط �~A�~Bط.

    إ�~F �~Cا�~Fت �~Dد�~J�~C أسئ�~Dة أ�~H إ�~F �~D�~E �~Jع�~E�~D ا�~Dح�~D �~J�~E�~C�~F�~C ا�~Dاتصا�~D ب�~Cائ�~F
    بشر�~J ع�~D�~I ع�~F�~Hا�~F ا�~Dدع�~E ا�~D�~A�~F�~J �~Gذا: tor-assistants@torproject.org

    --

    س�~Dا�~E! ر�~Hبات "GetTor" در خد�~Eت ش�~Eاست. 
    �~Eتاس�~Aا�~F�~G �~Eا �~F�~E�~L ت�~Hا�~F�~L�~E با ا�~L�~F آدرس با ش�~Eا در ارتباط باش�~L�~E. ش�~Eا با�~Lست�~L در 
    GMAIL.COM �~Lا در YAHOO.CN حساب باز کرد�~G �~H از طر�~L�~B �~Lک�~L از آ�~F آدرس�~Gا با �~Eا 
    �~Eکاتب�~G ک�~F�~Lد.
    
    �~Eا �~A�~Bط درخ�~Hاست�~Gا�~L�~L را �~E�~Hرد بررس�~L �~Bرار �~E�~L د�~G�~L�~E ک�~G سر�~H�~Lس پست ا�~Dکتر�~H�~F�~Lک�~L آ�~F�~Gا 
    "DKIM" را پشت�~Lبا�~F�~L ک�~Fد. "DKIM" ا�~L�~F ا�~Eکا�~F را ب�~G �~Eا �~E�~L د�~Gد تا اط�~E�~L�~Fا�~F �~Lاب�~L�~E ک�~G 
    آدرس �~E�~Fدرج در �~Bس�~Eت  "From"�~L �~G�~Eا�~F آدرس�~L است ک�~G �~Fا�~E�~G از آ�~F ب�~G �~Eا ارسا�~D شد�~G 
    است. 
    
    (در �~Gر ص�~Hرت عذرخ�~Hا�~G�~L �~Eا را پذ�~Lرا باش�~Lد. از آ�~Fجا�~L�~Lک�~G ا�~L�~E�~L�~D ش�~Eا DKIM را 
    پشت�~Lبا�~F�~L �~F�~E�~L ک�~Fد�~L �~Eا ا�~L�~F ت�~Hض�~Lح ک�~Hتا�~G را ارسا�~D �~F�~E�~Hد�~G �~H ا�~L�~F آدرس ا�~L�~E�~L�~D را 
    بز�~Hد�~L از �~A�~Gرست آدرس�~Gا�~L خ�~Hد خارج �~E�~L ک�~F�~L�~E.) 
    
    �~Dط�~Aا ب�~G ا�~L�~F �~Fکت�~G ت�~Hج�~G داشت�~G باش�~Lد ک�~G در حا�~D حاضر ا�~L�~E�~L�~D �~Gا�~L �~Eبت�~F�~L بر HTML �~Lا 
    64 ب�~Lت�~L�~L �~Bاب�~D بررس�~L �~F�~E�~L باش�~Fد. ب�~Fابرا�~L�~F ا�~L�~E�~L�~D �~Gا�~L خ�~Hد را ب�~G ص�~Hرت �~Eت�~F ساد�~G 
    ارسا�~D �~F�~Eا�~L�~Lد. 
    
    �~F�~Fا�~F�~F�~G س�~Hا�~D�~L دار�~Lد �~Lا بر�~Fا�~E�~G د�~Fار اشکا�~D ب�~Hد�~G �~H کار �~F�~E�~L ک�~Fد �~L با �~Bس�~Eت 
    پشت�~Lبا�~F�~L با آدرس ز�~Lر ت�~Eاس بگ�~Lر�~Lد تا �~Lک ا�~Fسا�~F ب�~G س�~Hا�~D ش�~Eا پاسخ د�~Gد:
    tor-assistants@torproject.org

    --

    Olá! Este é o robot "GetTor".
    
    Infelizmente, não respondemos neste endereço, pelo que é
    recomendado criar uma conta no Gmail ou Hotmail e enviar a mensagem de um 
    desses serviços.
    
    Só processamos emails de serviços que suportam "DKIM",
    que é uma forma de verificar que o endereço do "Remetente" é válido e se foi 
    mesmo esse a enviar o email.
    
    (Pedimos desculpa se não solicitou este email. Como a sua mensagem é de um 
    serviço que não suporta  DKIM, estamos a enviar esta curta explicação, e 
    depois este endereço de email será ignorado.)
    
    Actualmente não suportamos emails com HTML or Base64, pelo que terá que 
    utilizar apenas texto (plain text).
    
    Se tiver alguma dúvida, pode contactar um humano no seguinte endereço: 
    tor-assistants@torproject.org

    --

    �~Wд�~@ав�~A�~Bв�~Cй�~Bе! Э�~Bо "�~@обо�~B GetTor".
    
    �~Z �~Aожалени�~N, м�~K не �~Aможем о�~Bве�~Bи�~B�~L вам на �~M�~Bо�~B ад�~@е�~A. �~R�~K должн�~K �~Aозда�~B�~L
       �~A�~Gе�~B в GMAIL.COM или в YAHOO.COM и о�~Bп�~@авл�~O�~B�~L по�~G�~B�~C из 
        одного из �~M�~Bи�~E �~A�~Gе�~Bов.
    
    �~\�~K �~Bол�~Lко об�~@аба�~B�~Kваем зап�~@о�~A�~K из по�~G�~Bов�~K�~E �~Aл�~Cжб подде�~@жива�~N�~Iи�~E "DKIM",
    ко�~Bо�~@а�~O �~Oвл�~Oе�~B�~A�~O �~D�~Cнк�~Fией �~Mлек�~B�~@онной по�~G�~B�~K, позвол�~O�~N�~Iа�~O нам �~Cбеди�~B�~L�~A�~O в 
    �~Bом, �~G�~Bо ад�~@е�~A в
    �~A�~B�~@оке "�~^�~B" дей�~A�~Bви�~Bел�~Lно о�~B �~Bого, к�~Bо о�~Bо�~Aлал по�~G�~B�~C.
    
     (�~\�~K п�~@ино�~Aим извинени�~O, е�~Aли в�~K не п�~@о�~Aили �~M�~Bого пи�~A�~Lма. Так как ва�~Hе  
    email из �~Aе�~@ви�~Aа
    ко�~Bо�~@�~Kй не и�~Aпол�~Lз�~Cе�~B DKIM, м�~K о�~Bп�~@авл�~Oем к�~@а�~Bкое об�~J�~O�~Aнение,
    и далее м�~K п�~@оигно�~@и�~@�~Cем �~M�~Bо�~B ад�~@е�~A �~Mлек�~B�~@онной по�~G�~B�~K ден�~L или два.)
    
    �~_ожал�~Cй�~A�~Bа о�~Bме�~B�~L�~Bе, �~G�~Bо в на�~A�~Bо�~O�~Iее в�~@ем�~O м�~K не можем об�~@або�~Bа�~B�~L HTML 
    пи�~A�~Lма или базов�~Kе 64
    по�~G�~B�~C. �~R�~K должн�~K б�~Cде�~Bе по�~Aла�~B�~L об�~K�~Gн�~Kй �~Bек�~A�~B (plain text).
    
    �~U�~Aли �~C ва�~A воп�~@о�~A�~K или �~G�~Bо �~Bо не �~A�~@або�~Bало, в�~K може�~Bе �~Aв�~Oза�~B�~L�~A�~O 
    �~A жив�~Kм п�~@ед�~A�~Bави�~Bелем по �~M�~Bом�~C �~Mлек�~B�~@онном�~C ад�~@е�~A�~C:tor-assistants@torproject.org

    --

       �| 好!�~Y�~G~L�~X��~@~\GetTor�~@~]�~G��~J��~[~^�~M�~@~B

       �~H�~J��~I�~L�~H~Q们�~M对�~Y个�~\��~]~@�~[�~L�~[~^�~M�~L�~B��~T�~@~Z�~G
       GMAIL.COM�~H~Vyahoo.cn�~Z~D账�~H�使�~T��~H~Q们�~Z~D�~\~M�~J��~@~B

       �~H~Q们�~A�~B�~I~@�~D�~P~F�~B�件请�~B�~Z~D�~T��~B��~\~M�~J��~U~F�~E须�~T��~L~A�~@~\DKIM�~@~]
       �~C帮�~J��~H~Q们�~L�~A�~B�件�~X��~P��~\~_�~Z~D�~]��~G��~N�~B��~Z~D�~B�箱�~@~B

       (�~B�~^~\�~B�没�~\~I�~P~Q�~H~Q们�~O~Q�~@~A�~G�~B�件请�~B�~L对此�~[~^�~M�~H~Q们�~H�~J��~I�~@~B
      �~[| 为�~B��~Z~D�~B�件�~\~M�~J��~U~F�~M�~O~P�~[DKIM�~J~_�~C��~L�~\~I人�~O��~C�伪�~@| �~F�| �~B��~]~@
      �~H~Q们�~Y�~G~L�~O~Q�~@~A�~@�~]��~@�~_��~Z~D�~@~Z�~_��~L并�~F�~\�以�~P~N�~Z~D�~G| 天�~G~L忽�~U�该�~B��~]~@�~L
      以�~E~M形�~H~P�~^~C�~\��~[~^�~M�~@~B)

       请注�~D~O�~L�~H~Q们�~[��~I~M�~W| �~U�~D�~P~FHTML�~H~VBase64�~V�| ~A�~Z~D�~B�件�~L�~B��~O��~C��~O~Q�~@~A纯�~V~G�~\�请�~B�~@~B

       �~B�~^~\�~B��~A~G�~H�任�~U�~W��~X请�~A~T系�~H~Q们�~Z~D�~J~@�~\��~T��~L~A�~B�箱�~Z
         tor-assistants@torproject.org
        """

# Short string to build mails follow
hello_gettor = _("""
    Hello, This is the "GetTor" robot.

    Thank you for your request.

    """)
help_dkim_1 = _("""
    Unfortunately, we won't answer you at this address. You should make
    an account with GMAIL.COM or YAHOO.CN and send the mail from
    one of those.

    """)
help_dkim_2 = _("""
    We only process requests from email services that support "DKIM",
    which is an email feature that lets us verify that the address in the
    "From" line is actually the one who sent the mail.

    """)
help_dkim_3 = _("""
    (We apologize if you didn't ask for this mail. Since your email is from
    a service that doesn't use DKIM, we're sending a short explanation,
    and then we'll ignore this email address for the next day or so.)

    """)
help_dkim_4 = _("""
    Please note that currently, we can't process HTML emails or base 64
    mails. You will need to send plain text.

    """)

help_dkim_5 = _("""
    If you have any questions or it doesn't work, you can contact a
    human at this support email address: tor-assistants@torproject.org

    """)
choose_package_1 = _("""
    I will mail you a Tor package, if you tell me which one you want.
    Please select one of the following package names:

    """)
avail_packs = """
        tor-browser-bundle
        macosx-i386-bundle
        macosx-ppc-bundle
        tor-im-browser-bundle
        source-bundle
    
    """
choose_package_2 = _("""
    Please reply to this mail (to gettor@torproject.org), and tell me
    a single package name anywhere in the body of your email.

    """)
obtain_localized_head = _("""
    OBTAINING LOCALIZED VERSIONS OF TOR
    """)
obtain_locallized_underline = """
    ===================================

    """
obtain_localized_1 = _("""
    To get a version of Tor translated into your language, specify the
    language you want in the address you send the mail to:

    """)
obtain_localized_2 = """
        gettor+zh@torproject.org

    """
obtain_localized_3 = _("""
    This example will give you the requested package in a localized
    version for Chinese. Check below for a list of supported language
    codes.

    """)
list_of_langs_head = _("""
    List of supported locales:
    """)
list_of_langs_underline = """
    -------------------------

    """
list_of_langs_1 = _("""
    Here is a list of all available languages:

    """)
list_of_langs_2 = _("""
    gettor+ar@torproject.org:     Arabic
    gettor+de@torproject.org:     German
    gettor+en@torproject.org:     English
    gettor+es@torproject.org:     Spanish
    gettor+fa@torproject.org:     Farsi (Iran)
    gettor+fr@torproject.org:     French
    gettor+it@torproject.org:     Italian
    gettor+nl@torproject.org:     Dutch
    gettor+pl@torproject.org:     Polish
    gettor+ru@torproject.org:     Russian
    gettor+zh@torproject.org:     Chinese

    """)
list_of_langs_3 = _("""
    If you select no language, you will receive the English version.

    """)
support = _("""
    SUPPORT
    """)
support_underline = """
    =======
    """
support_email = _("""
    If you have any questions or it doesn't work, you can contact a
    human at this support email address: tor-assistants@torproject.org

    """)
package_mail_1 = _("""
    Here's your requested software as a zip file. Please unzip the
    package and verify the signature.

    """)
package_mail_2 = _("""
    Hint: If your computer has GnuPG installed, use the gpg
    commandline tool as follows after unpacking the zip file:

    """)
package_mail_3 = _("""
       gpg --verify <packagename>.asc <packagename>

    """)
package_mail_4 = _("""
    The output should look somewhat like this:

    """)
package_mail_5 = """
       gpg: Good signature from "Roger Dingledine <arma@mit.edu>"

    """
package_mail_6 = _("""
    If you're not familiar with commandline tools, try looking for
    a graphical user interface for GnuPG on this website:

    """)
package_mail_7 = """
       http://www.gnupg.org/related_software/frontends.html

    """
package_mail_8 = _("""
    If your Internet connection blocks access to the Tor network, you
    may need a bridge relay. Bridge relays (or "bridges" for short)
    are Tor relays that aren't listed in the main directory. Since there
    is no complete public list of them, even if your ISP is filtering
    connections to all the known Tor relays, they probably won't be able
    to block all the bridges.

    """)
package_mail_9 = _("""
    You can acquire a bridge by sending an email that contains "get bridges"
    in the body of the email to the following email address:
    bridges@torproject.org

    """)
package_mail_10 = _("""
    It is also possible to fetch bridges with a web browser at the following
    url: https://bridges.torproject.org/

    """)
split_package_1 = _("""
    IMPORTANT NOTE:
    Since this is part of a split-file request, you need to wait for
    all split files to be received by you before you can save them all
    into the same directory and unpack them by double-clicking the
    first file.

    """)
split_package_2 = _("""
    Packages might come out of order! Please make sure you received
    all packages before you attempt to unpack them!

    """)
delay_alert_1 = _("""
    Thank you for your request. It was successfully understood. Your request is
    currently being processed. Your package should arrive within the next ten
    minutes.

    """)
delay_alert_2 = _("""
    If it doesn't arrive, the package might be too big for your mail provider.
    Try resending the mail from a gmail.com or yahoo.cn account. Also,
    try asking for tor-browser-bundle rather than tor-im-browser-bundle,
    since it's smaller.

    """)
error_mail = _("""
    Unfortunately we are currently experiencing problems and we can't fulfill
    your request right now. Please be patient as we try to resolve this issue.

    """)

# Build the actual mail texts
packagehelpmsg = hello_gettor + choose_package_1 + avail_packs + choose_package_2 + \
                 obtain_localized_head + obtain_localized_underline + \
                 obtain_localized_1 + obtain_localized_2 + obtain_localized_3 + \
                 list_of_langs_head + list_of_langs_underline + \
                 list_of_langs_1 + list_of_langs_2 + list_of_langs_3 + \
                 support + support_underline + support_email

helpmsg = hello_gettor + \
          help_dkim_1 + help_dkim_2 + help_dkim_3 + help_dkim_4 + help_dkim_5 + \
          support_email


packagemsg = hello_gettor + \
             package_mail_1 + package_mail_2 + package_mail_3 + package_mail_4 + \
             package_mail_5 + package_mail_6 + package_mail_7 + package_mail_8 + \
             package_mail_9 + package_mail_10 + \
             support_email


splitpackagemsg = hello_gettor + \
                  split_package_1 + split_package_2 + \
                  package_mail_1 + package_mail_2 + package_mail_3 + package_mail_4 + \
                  package_mail_5 + package_mail_6 + package_mail_7 + package_mail_8 + \
                  package_mail_9 + package_mail_10 + \
                  support_email


delayalertmsg = hello_gettor + \
                delay_alert_1 + delay_alert_2 + \
                support_email

mailfailmsg = hello_gettor + \
              support_email


