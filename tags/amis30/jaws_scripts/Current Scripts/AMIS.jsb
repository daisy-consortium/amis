JFW Script File                                                           X>  �    autostartevent  $  firsttime         
          &  firsttime        &  jawsspeech      Welcome to AMIS window         say        for a help list of Jaws specific commands press  insert h          say       		 for help for AMIS commands press F1        say        AMIS is ready          say           AMIS Window is active          say            isamisselfvoiceonfromtitle       
              JAWS Muted         sayformattedmessage         speechoff            &  jawsspeech          speechon            &  jawsspeech          amisactivatevirtualcursurswitch         getappfilepath  &  amisdirectory      $  amisdirectory        getappfilename         stringreplacesubstrings &  amisdirectory        isamishasnewbook         
          exitamistextreadingmodes             x    amisactivatevirtualcursurswitch         getfocus      getcontrolid          
     $  stocmode     On  
          �    getjcfoption          
          �         setdefaultjcfoption          $  stocmode     Off 
          �    getjcfoption         
          �          setdefaultjcfoption                8    isamishasnewbook         getapptitle '      %    Default view mode -   stringcontains  '  %        
        %    Basic view mode -     stringcontains  '        %   %    stringchopright '   $  g_stitle    %   
     %   &  g_stitle            	               	         x    windowdestroyedevent          %     windowdestroyedevent                  getfocus      getrealwindow     getwindowname   '  $  tempjawsspeech       
  # � $  jawsspeech        
  
  #    %   Open      stringcontains        
  
          speechoff             ExitTextModeOnNewBook          schedulefunction          �     windowactivatedevent          %     windowactivatedevent           UnMuteJawsSpeechOnOpenDialog           schedulefunction          <    unmutejawsspeechonopendialog    $  jawsspeech        
                getfocus      getrealwindow     getwindowname   '        inhjdialog  " �    %    Open      stringcontains        
  
          speechon            &  tempjawsspeech     %     saystring               x     exittextmodeonnewbook        isamishasnewbook         
          exitamistextreadingmodes                 autofinishevent      �    getjcfoption          
          �         setdefaultjcfoption            speechon       $  snavigationmode  On  
          exitamisfinenavigationmode            Leaving AMIS           say       0     $playpause      Space     typekey    T     $increasevolume      typecurrentscriptkey            stopspeech        P     $volumedown      typecurrentscriptkey            stopspeech        x     $fasternum            Faster   Faster    sayformattedmessage         typecurrentscriptkey          t     $faster           Faster   Faster    sayformattedmessage         typecurrentscriptkey          x     $slowernum            Slower   Slower    sayformattedmessage         typecurrentscriptkey          t     $slower           Slower   Slower    sayformattedmessage         typecurrentscriptkey          �     $normalspeed              Normal Speed     Normal Speed      sayformattedmessage         typecurrentscriptkey          P    $previoussection         ispccursor  # P $  stocmode     ON  
  
  # x      userbufferisactive    
          typecurrentscriptkey            stopspeech             priorline           getcursorrow    '   %   $  pastcursorpositiony 
        %   &  pastcursorpositiony      sayline          L    $nextsection         ispccursor  # L $  stocmode     ON  
  
  # t      userbufferisactive    
          typecurrentscriptkey            stopspeech             nextline            getcursorrow    '   %   $  pastcursorpositiony 
        %   &  pastcursorpositiony      sayline          �     $previousphrase      ispccursor  # L $  stocmode     ON  
  
  # t      userbufferisactive    
          typecurrentscriptkey            stopspeech             priorcharacter          saycharacter             �     $nextphrase      ispccursor  # H $  stocmode     ON  
  
  # p      userbufferisactive    
          typecurrentscriptkey            stopspeech             nextcharacter           saycharacter             8    $gotosidebar         getactivecursor '        pccursor            checkviewsfromtitle '  %   Default 
             getcurrentwindow      getwindowname    tree1   
     $  snavigationmode  On  
         Side Bar      saystring             Already in side navigation bar    saystring                 typecurrentscriptkey                 delay           pccursor               getcurrentwindow      getwindowname    tree1   
              Move to side bar     Side Bar      sayformattedmessage               exitamistextreadingmodes          %   Basic   
             		 There is no side bar in basic view  		 There is no side bar in basic view    sayformattedmessage       %     setactivecursor          �     $prevpage        ispccursor  # H $  stocmode     ON  
  
  # p      userbufferisactive    
          typecurrentscriptkey            stopspeech             priorword           sayword          �     $nextpage        ispccursor  # H $  stocmode     ON  
  
  # p      userbufferisactive    
          typecurrentscriptkey            stopspeech             nextword            sayword          ,     $sayview         sayviews          t    sayviews         checkviewsfromtitle  Default 
             		 Now you are in default view mode     Default View Mode     sayformattedmessage            checkviewsfromtitle  Basic   
              Now you are in basic view mode with no side bar.     Basic view mode   sayformattedmessage            restorecursor         �     checkviewsfromtitle            getfocus      getappmainwindow      getwindowname   '      %    Basic     stringcontains      Basic      	         %    Default   stringcontains      Default    	             $toggleviews         typecurrentscriptkey                 delay              getfocus      getcontrolid         
          stopspeech          sayviews          $  snavigationmode  On  
          exitamisfinenavigationmode               $hotkeyhelp      userbufferisactive          userbufferdeactivate               (   �� The keyboard shortcuts are:
Play/Pause %KeyFor(PlayPause)
Faster Rate %KeyFor(Faster)
Faster Rate using NumPad %KeyFor(FasterNum)
Slower Rate %KeyFor(Slower)
Slower Rate using NumPad %KeyFor(SlowerNum)
Normal speed rate %KeyFor(NormalSpeed)
Decrease Volume %KeyFor(VolumeDown)
Increase Volume %KeyFor(IncreaseVolume)
Go to next phrase %KeyFor(NextPhrase)
Go to previous phrase %KeyFor(PreviousPhrase)
Go to Next Section %KeyFor(NextSection)
Go to previous section %KeyFor(PreviousSection)
Go to Next Page %KeyFor(NextPage)
Go to previous Page %KeyFor(PrevPage)
Toggle views between default view and basic view mode %KeyFor(ToggleViews)
Say Current view %KeyFor(SayView)
Go to side bar %KeyFor(GoToSideBar)
Move to main window %KeyFor(MoveToTextWindow )
Toggle Jaws Speech%KeyFor(ToggleJawsSpeech)
Fine Navigation %KeyFor(FineNavigation)
Read text Only Book%KeyFor(ReadAsTextOnly )

Pres	s ESC to close this message.
Press %keyFor(HotKeyHelp) for JAWS hot key help   sayformattedmessage    $  jawsspeech        
  # �     userbufferisactive  
          speechon            &  tempjawsspeech      JAWS Hotkey Help      saystring           jawstopoffile            <    $finenavigation $  jawsspeech        
          &  jawsspeech       speechon            &  tempjawsspeech          isplaying        
         Space     typekey           delay                   delay           getactivecursor '        jawscursor          savecursor          routejawstopc           jawstopoffile                setrestriction             �        getamishighlightbkcolor   rgbhextocolor                 findcolors       
          routeinvisibletojaws            restorecursor                 getamishighlightbkcolor   rgbhextocolor     sayhighlight        On  &  snavigationmode        Not found     saystring           restorecursor         %     setactivecursor          �    sayhighlight            invisiblecursor              setrestriction           '       getcolorbackground  %   
  # � %    
   
  
          priorline      %       
  '   d         getcolorbackground  %   
          sayline             '       getcolorbackground  %   
  # `%       
  
          nextword       %       
  '   $        sayline          �     $finenavigationexit $  snavigationmode  On  
          exitamisfinenavigationmode            Not in fine Navigation mode   saystring            X    exitamisfinenavigationmode            setrestriction          pccursor        Off &  snavigationmode          Exiting Fine Navigation Mode     Exiting fine navigation   sayformattedmessage    $  tempjawsspeech       
           &  jawsspeech       speechoff            &  tempjawsspeech        �    $togglejawsspeech   $  jawsspeech        
          &  jawsspeech       isamisselfvoiceonfromtitle       
         Ctrl+Shift+g      typekey         speechon                Jaws Speech for Amis, on     on    sayformattedmessage             &  jawsspeech           Jaws Speech for Amis, off    off   sayformattedmessage         isamisselfvoiceonfromtitle        
         Ctrl+Shift+g      typekey         speechoff                isamisselfvoiceonfromtitle             getfocus      getappmainwindow      getwindowname   '      %    Not self-voicing      stringcontains           '        %    Self-voicing      stringcontains          '     %     	      �     isplaying              getfocus      getappmainwindow      getwindowname   '      %    Paused    stringcontains           '        %    Playing   stringcontains          '          '     %     	          $readastextonly $  snavigationmode  On  
          exitamisfinenavigationmode                   getcursorcol         getcursorrow      getwindowatpoint      getcontrolid      �  
  #      checkviewsfromtitle  Default 
  
          pccursor            isplaying        
         Space     typekey              delay                getobjectname   '        gettreeviewlevel    '     %     stringstripallblanks    '            moving to text window...     Text Window...    sayformattedmessage         speechoff          Control+T     typekey           delay                   pccursor            �    getjcfoption          
          �         setdefaultjcfoption               getfocus      getcontrolid          
               refresh              delay            '       $movetofirstheading            getheadingcount '     %     istargethtmlheading       
  # (%  %  
  
          $movetonextheading  %       
  '   �        isplaying        
         Space     typekey         speechon                 delay           sayline                   Text Window...   Text Window...    sayformattedmessage         �    getjcfoption          
          �         setdefaultjcfoption              delay              nextline            sayline        ON  &  stocmode       h     $textonlymodeexit   $  stocmode     ON  
          exitamistextonlyreadingmode              exitamistextonlyreadingmode  OFF &  stocmode         refresh         �    getjcfoption         
          �          setdefaultjcfoption         stopspeech           		 Exiting Read text only book mode      saystring         �     exitamistextreadingmodes    $  stocmode     ON  
          exitamistextonlyreadingmode       $  snavigationmode  On  
          exitamisfinenavigationmode           T    $movetotextwindow        typecurrentscriptkey                 delay           �    getjcfoption         
          �          setdefaultjcfoption         stopspeech                 Moving to main window    Main window   sayformattedmessage         exitamistextreadingmodes          `    istargethtmlheading         getcurrentheading   '     %    stringstripallblanks    '  %  %   
          isamistexthighlighted        
             	           nextline            getamishighlightbkcolor '  %       
     %  &  preferencehighlightbkcolor          getcolorbackground     $  preferencehighlightbkcolor    rgbhextocolor   
             	           priorline           nextsentence            getcolorbackground     $  preferencehighlightbkcolor    rgbhextocolor   
             	                     	      l    isamistexthighlighted                   getelementdescription   '        getamishighlightbkcolor '  %       
     %  &  preferencehighlightbkcolor      BACKGROUND-COLOR:    #   
     $  preferencehighlightbkcolor    stringlower 
  '     %   %    stringcontains        
             	               	         �     getamishighlightbkcolor     highlight-bg      getamispreferencevalue  '      %    #     stringcontains        %          stringchopleft  '      %      	      �    getamispreferencevalue        $  amisdirectory    settings\config\amisPrefs.xml   
    getfiletextinstring '     %  %     stringcontains  '     %  %    stringchopleft  '     %   />    stringcontains  '     %  %       
    stringleft  '     %   value=    stringcontains  '     %  %       
    stringchopleft  '  %     	      �     objectcreate          %          createobjectex  '  %          %           createobjectex  '     %          %     getobject   '     %     	      �     getfiletextinstring        Scripting.FilesystemObject    objectcreate    '  %    %                opentextfile    '  %      readall '  %      close      %  '  %  '  %     	      �     $saytitlehook   $  jawsspeech        
          speechon            $saywindowtitle          JAWS Muted   JAWS Muted    sayformattedmessage         speechoff              $saywindowtitle       