<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Machado de Assis.net | Pesquisa ao banco de dados</title>

<script language="JavaScript"
type="text/JavaScript">
<!

function MM_jumpMenu(targ,selObj,restore){ //v3.0
  eval(targ+".location='"+selObj.options[selObj.
  selectedIndex].value+"'");
  if (restore) selObj.selectedIndex=0;
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?")
  )>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document;
	n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<
  d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++)
  x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n);
return x;
}

function MM_jumpMenuGo(selName,targ,restore){ //v3.0
  var selObj = MM_findObj(selName);
  if (selObj) MM_jumpMenu(targ,selObj,restore);
}

</script>

<script src="cbboxSearch.js" type="text/javascript"></script>

<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />

<link rel="stylesheet" type="text/css" href="css/dtb_estilos.css">


   <script>
     var ie = /msie/i.test(navigator.userAgent);
     var ieBox = ie && (document.compatMode == null || document.compatMode == "BackCompat");

     function checkSize() {
       var canvasEl = ieBox ? document.body : document.documentElement;
       var w = window.innerWidth || canvasEl.clientWidth;
       var h = window.innerHeight || canvasEl.clientHeight;

      // document.getElementById("teste").style.width = Math.max(0, w - 50) + "px";
      // document.getElementById("teste").style.height = Math.max(0, h - 100) + "px";
       document.getElementById("areaPesquisa").style.width = Math.max(0, w - 50) + "px";
       document.getElementById("areaPesquisa").style.height = Math.max(0, h - 100) + "px";
     }

     window.onload = checkSize;
     window.onresize = checkSize;
   </SCRIPT>

<!-- Abre janela:  Alertas -->
<script language="JavaScript"> function newJanelaA(desktopURL){var desktop = window.open( desktopURL, "_blank", "toolbar=no,location=no,status=no,menubar=no,resizable=no,scrollbars=no,top=300,left=300,width=422,height=200");} </script>

<!-- Abre janela:  Alertas -->
<script language="JavaScript"> function newJanelaA(desktopURL){var desktop = window.open( desktopURL, "_blank", "toolbar=no,location=no,status=no,menubar=no,resizable=no,scrollbars=no,top=300,left=300,width=422,height=200");} </script>

</head>

<script language="Javascript">

function opcao_busca(op) {
   if (op == 1){
      document.getElementById('FORM1').submit();
   }
}

function Hab(valor) {
  if( valor == 1 ){ // selecionou CONTO
    document.getElementById("Selromance").disabled = true;
    document.getElementById("Selconto").disabled = false;

    zera_romance = 1
    zera_conto_romance = 1
    zera_conto = 0
  }else if( valor == 2){ // selecionou ROMANCE
    document.getElementById("Selromance").disabled = false;
    document.getElementById("Selconto").disabled = true;
    zera_conto = 1
    zera_conto_romance = 1
    zera_romance = 0
  }else if( valor == 3){ // selecionou CONTO E ROMANCES
    document.getElementById("Selromance").disabled = true;
    document.getElementById("Selconto").disabled = true;
    zera_conto = 1
    zera_romance = 1
    zera_conto_romance = 0
  }else if( valor == 4){ // O SELECT SELCONDICAO N�O FOI PREENCHIDO
    document.getElementById("Selcondicao").visible = false;
   //document.getElementById("Selconto").disabled = true;
   // zera_conto = 1
   // zera_romance = 1
   // zera_conto_romance = 0
  }
}


</script>

<body>
   

  <!-- para os bot�es -->
   




<div id="headBG">
<div id="headFigON"></div>
<div id="figIndex"></div>
<div id="headTitu"><img src="figs/head_dtb_titu.gif" alt="citacoes e alusoes na ficcao de Machado de Assis" width="522" height="28" /></div>

<div id="menu">
  <table width="199" height="43" border="0" cellpadding="0" cellspacing="0">
    <tr>
      <td width="90"><a href="dtb_index.asp"><img src="figs/m_dtb_pesON.gif" alt="dtb_index.asp" width="90" height="43" border="0" /></a></td>
      <td width="23"><img src="figs/m_dtb_pesON_R.gif" width="23" height="43" /></td>
      <td width="63"><a href="dtb_ajuda.asp"><img src="figs/m_dtb_aju.gif" alt="dtb_ajuda.htm" width="63" height="43" border="0" /></a></td>
      <td width="23"><img src="figs/m_dtb_aju_R.gif" width="23" height="43" /></td>
      <td>&nbsp;</td>
    </tr>
  </table>
</div>

<div class="memu2">
 <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td class="menuTop" ><a href="index.htm">IN&Iacute;CIO</a><img src="figs/xvazio.gif" width="18" height="10"><a href="links.asp">LINKS</a><img src="figs/xvazio.gif" width="18" height="10"><a href="equipe.asp">EQUIPE</a><img src="figs/xvazio.gif" width="18" height="10"><a href="contato.asp">CONTATO</a></td>
    </tr>
  </table>
</div>
</div>

<div id="areaPesquisa">
  <table width="756" border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td ><FORM NAME="FORM1" ID="FORM1" METHOD="Get" ACTION="dtb_index.asp">
      <table width="720" border="0" cellpadding="0" cellspacing="0" id="pesquisaForm1">
       <!-- <tr> -->
          <td colspan="3" class="formTitu1L">Selecione</td>
          <!-- <td class="vazio">&nbsp;</td> -->
          <td class="dots"><img src="figs/form_dots23.gif" width="18" height="18" /></td>
          <td class="formTitu2L">Obra de Machado de Assis </td>
          <!-- <td class="vazio">&nbsp;</td> -->
          <td class="dots"><img src="figs/form_dots23.gif" width="18" height="18" /></td>
          <td class="formTitu2L">Selecione o campo de busca </td>
        <!-- </tr> -->
         <!-- Selecao de Contos -->
        <tr>
          <td class="dots"><img src="figs/form_dots123.gif" width="18" height="18" /></td>
          
             <td><input name="radiobutton" type="radio" class="dots" value="conto" onclick="Hab(1);"/></td>
          
          
          <td class="formTxL">Contos</td>
          <!-- <td class="vazio">&nbsp;</td> -->
           <td class="dots"><img src="figs/form_dots123.gif" width="18" height="18" />
           </td>
          <td > <div class="pesquisa1">
       <select name="Selconto" size="1" id="Selconto" onkeypress="cbboxSearch(this, event); return false;">
       <OPTION value= 0 Selected>Contos: Selecione --&gt;</option>
       <option  value= 30 class="stit" >Todos os Contos</option>
       <option>-------------------------------------------------------</option>
       <option  value= 21 class="stit" >Contos fluminenses</option>
       <option value=211 >&nbsp;&ndash;&nbsp;Miss Dollar</option>
       <option value=212 >&nbsp;&ndash;&nbsp;Lu�s Soares</option>
       <option value=213 >&nbsp;&ndash;&nbsp;A mulher de preto</option>
       <option value=214 >&nbsp;&ndash;&nbsp;O segredo de Augusta</option>
       <option value=215 >&nbsp;&ndash;&nbsp;Confiss�es de uma vi�va mo�a</option>
       <option value=216 >&nbsp;&ndash;&nbsp;Linha reta e linha curva</option>
       <option value=217 >&nbsp;&ndash;&nbsp;Frei Sim�o</option>
     <option>-------------------------------------------------------</option>
     <option value= 22 class="stit" >Hist�rias da meia-noite
       <option value=221 >&nbsp;&ndash;&nbsp;Advert�ncia</option>
       <option value=222 >&nbsp;&ndash;&nbsp;A parasita azul</option>
       <option value=223 >&nbsp;&ndash;&nbsp;As bodas de Lu�s Duarte</option>
       <option value=224 >&nbsp;&ndash;&nbsp;Ernesto de tal</option>
       <option value=225 >&nbsp;&ndash;&nbsp;Aurora sem dia</option>
       <option value=226 >&nbsp;&ndash;&nbsp;O rel�gio de ouro</option>
       <option value=227 >&nbsp;&ndash;&nbsp;Ponto de vista</option>
     <option>-------------------------------------------------------</option>
     <option value= 23 class="stit" >Pap�is avulsos
       <option value=231 >&nbsp;&ndash;&nbsp;Advert�ncia</option>
       <option value=232 >&nbsp;&ndash;&nbsp;O alienista</option>
       <option value=233 >&nbsp;&ndash;&nbsp;Teoria do medalh�o</option>
       <option value=234 >&nbsp;&ndash;&nbsp;A chinela turca</option>
       <option value=235 >&nbsp;&ndash;&nbsp;Na arca</option>
       <option value=236 >&nbsp;&ndash;&nbsp;Dona Benedita</option>
       <option value=237 >&nbsp;&ndash;&nbsp;O segredo do bonzo</option>
       <option value=238 >&nbsp;&ndash;&nbsp;O anel de Pol�crates</option>
       <option value=239 >&nbsp;&ndash;&nbsp;O empr�stimo</option>
       <option value=2310 >&nbsp;&ndash;&nbsp;A seren�ssima rep�blica</option>
       <option value=2311 >&nbsp;&ndash;&nbsp;O espelho</option>
       <option value=2312 >&nbsp;&ndash;&nbsp;Uma visita de Alcib�ades</option>
       <option value=2313 >&nbsp;&ndash;&nbsp;Verba testament�ria</option>
     <option>-------------------------------------------------------</option>
     <option value= 24 class="stit" >Hist�rias sem data
       <option value=241 >&nbsp;&ndash;&nbsp;Advert�ncia da 1� edi��o</option>
       <option value=242 >&nbsp;&ndash;&nbsp;A igreja do Diabo</option>
       <option value=243 >&nbsp;&ndash;&nbsp;O lapso</option>
       <option value=244 >&nbsp;&ndash;&nbsp;�ltimo cap�tulo</option>
       <option value=246 >&nbsp;&ndash;&nbsp;Cantiga de esponsais</option>
       <option value=247 >&nbsp;&ndash;&nbsp;Singular ocorr�ncia</option>
       <option value=248 >&nbsp;&ndash;&nbsp;Galeria p�stuma</option>
       <option value=249 >&nbsp;&ndash;&nbsp;Cap�tulo dos chap�us</option>
       <option value=2410 >&nbsp;&ndash;&nbsp;Conto alexandrino</option>
       <option value=2411 >&nbsp;&ndash;&nbsp;Primas de Sapucaia!</option>
       <option value=245 >&nbsp;&ndash;&nbsp;Uma senhora</option>
       <option value=2412 >&nbsp;&ndash;&nbsp;Anedota pecuni�ria</option>
       <option value=2413 >&nbsp;&ndash;&nbsp;Fulano</option>
       <option value=2414 >&nbsp;&ndash;&nbsp;A segunda vida</option>
       <option value=2415 >&nbsp;&ndash;&nbsp;Noite de almirante</option>
       <option value=2416 >&nbsp;&ndash;&nbsp;Manuscrito de um sacrist�o</option>
       <option value=2417 >&nbsp;&ndash;&nbsp;Ex cathedra</option>
       <option value=2418 >&nbsp;&ndash;&nbsp;A senhora do Galv�o</option>
       <option value=2419 >&nbsp;&ndash;&nbsp;As academias de Si�o</option>
     <option>-------------------------------------------------------</option>
     <option value= 25 class="stit" >V�rias hist�rias
       <option value=2518 >&nbsp;&ndash;&nbsp;Ep�grafe</option>
       <option value=251 >&nbsp;&ndash;&nbsp;Advert�ncia</option>
       <option value=252 >&nbsp;&ndash;&nbsp;A cartomante</option>
       <option value=253 >&nbsp;&ndash;&nbsp;Entre santos</option>
       <option value=254 >&nbsp;&ndash;&nbsp;Uns bra�os</option>
       <option value=255 >&nbsp;&ndash;&nbsp;Um homem c�lebre</option>
       <option value=256 >&nbsp;&ndash;&nbsp;A desejada das gentes</option>
       <option value=257 >&nbsp;&ndash;&nbsp;A causa secreta</option>
       <option value=258 >&nbsp;&ndash;&nbsp;Trio em l� menor</option>
       <option value=259 >&nbsp;&ndash;&nbsp;Ad�o e Eva</option>
       <option value=2510 >&nbsp;&ndash;&nbsp;O enfermeiro</option>
       <option value=2511 >&nbsp;&ndash;&nbsp;O diplom�tico</option>
       <option value=2512 >&nbsp;&ndash;&nbsp;Mariana</option>
       <option value=2513 >&nbsp;&ndash;&nbsp;Conto de escola</option>
       <option value=2514 >&nbsp;&ndash;&nbsp;Um ap�logo</option>
       <option value=2515 >&nbsp;&ndash;&nbsp;Dona Paula</option>
       <option value=2516 >&nbsp;&ndash;&nbsp;Viver!</option>
       <option value=2517 >&nbsp;&ndash;&nbsp;O c�nego ou metaf�sica do estilo</option>

      <option>-------------------------------------------------------</option>
     <option value= 26 class="stit"  >P�ginas recolhidas
       <option value=2610 >&nbsp;&ndash;&nbsp;Ep�grafe do livro</option>
       <option value=261 >&nbsp;&ndash;&nbsp;Pref�cio</option>
       <option value=262 >&nbsp;&ndash;&nbsp;O caso da vara</option>
       <option value=263 >&nbsp;&ndash;&nbsp;O dicion�rio</option>
       <option value=264 >&nbsp;&ndash;&nbsp;Um erradio</option>
       <option value=265 >&nbsp;&ndash;&nbsp;Eterno!</option>
       <option value=266 >&nbsp;&ndash;&nbsp;Missa do galo</option>
       <option value=267 >&nbsp;&ndash;&nbsp;Id�ias de can�rio</option>
       <option value=268 >&nbsp;&ndash;&nbsp;L�grimas de Xerxes</option>
       <option value=269 >&nbsp;&ndash;&nbsp;Pap�is velhos</option>

     <option>-------------------------------------------------------</option>
     <option value= 27 class="stit" >Rel�quias de casa velha
       <option value=271 >&nbsp;&ndash;&nbsp;Advert�ncia</option>
       <option value=272 >&nbsp;&ndash;&nbsp;Pai contra m�e</option>
       <option value=273 >&nbsp;&ndash;&nbsp;Maria Cora</option>
       <option value=274 >&nbsp;&ndash;&nbsp;Marcha f�nebre</option>
       <option value=275 >&nbsp;&ndash;&nbsp;Um capit�o de Volunt�rios</option>
       <option value=276 >&nbsp;&ndash;&nbsp;Suje-se gordo!</option>
       <option value=277 >&nbsp;&ndash;&nbsp;Umas f�rias</option>
       <option value=278 >&nbsp;&ndash;&nbsp;Evolu��o</option>
       <option value=279 >&nbsp;&ndash;&nbsp;P�lades e Orestes</option>
       <option value=2710 >&nbsp;&ndash;&nbsp;Anedota do cabriol�</option>
     <option>-------------------------------------------------------</option>
     <option value= 28 class="stit" >Outros contos
       <option value=281 >&nbsp;&ndash;&nbsp;A carteira</option>
       <option value=282 >&nbsp;&ndash;&nbsp;A chave</option>
       <option value=283 >&nbsp;&ndash;&nbsp;A heran�a</option>
       <option value=284 >&nbsp;&ndash;&nbsp;A id�ia de Ezequiel Maia</option>
       <option value=285 >&nbsp;&ndash;&nbsp;A igreja do Diabo</option>
       <option value=286 >&nbsp;&ndash;&nbsp;A inglesinha Barcelos</option>
       <option value=287 >&nbsp;&ndash;&nbsp;A m�goa do infeliz Cosme</option>
       <option value=288 >&nbsp;&ndash;&nbsp;A melhor das noivas</option>
       <option value=289 >&nbsp;&ndash;&nbsp;A mulher de preto</option>
       <option value=2810 >&nbsp;&ndash;&nbsp;A mulher p�lida</option>
       <option value=2811 >&nbsp;&ndash;&nbsp;A pianista </option>
       <option value=2812 >&nbsp;&ndash;&nbsp;A �ltima receita</option>
       <option value=2813 >&nbsp;&ndash;&nbsp;A vi�va Sobral</option>
       <option value=2814 >&nbsp;&ndash;&nbsp;Aires e Vergueiro</option>
       <option value=2815 >&nbsp;&ndash;&nbsp;Almas agradecidas</option>
       <option value=2816 >&nbsp;&ndash;&nbsp;Antes que cases...</option>
       <option value=2817 >&nbsp;&ndash;&nbsp;Ast�cias de marido</option>
       <option value=2818 >&nbsp;&ndash;&nbsp;Brincar com fogo</option>
       <option value=2819 >&nbsp;&ndash;&nbsp;Cantiga velha</option>
       <option value=2820 >&nbsp;&ndash;&nbsp;Casa Velha</option>
       <option value=2821 >&nbsp;&ndash;&nbsp;Casa, n�o casa</option>
       <option value=2822 >&nbsp;&ndash;&nbsp;Casada e vi�va</option>
       <option value=2823 >&nbsp;&ndash;&nbsp;Cinco mulheres</option>
       <option value=2824 >&nbsp;&ndash;&nbsp;Como se inventaram os almanaques</option>
       <option value=2825 >&nbsp;&ndash;&nbsp;Convers�o de um avaro</option>
       <option value=2826 >&nbsp;&ndash;&nbsp;Curta hist�ria</option>
       <option value=2827 >&nbsp;&ndash;&nbsp;Decad�ncia de dois grandes homens</option>
       <option value=2828 >&nbsp;&ndash;&nbsp;D�vida extinta</option>
       <option value=2829 >&nbsp;&ndash;&nbsp;Dona Jucunda</option>
       <option value=2830 >&nbsp;&ndash;&nbsp;Dona M�nica</option>
       <option value=2831 >&nbsp;&ndash;&nbsp;Encher tempo</option>
       <option value=2832 >&nbsp;&ndash;&nbsp;Entre duas datas</option>
       <option value=2833 >&nbsp;&ndash;&nbsp;Flor an�nima</option>
       <option value=2834 >&nbsp;&ndash;&nbsp;Folha rota</option>
       <option value=2835 >&nbsp;&ndash;&nbsp;Habilidoso</option>
       <option value=2836 >&nbsp;&ndash;&nbsp;Hist�ria comum</option>
       <option value=2837 >&nbsp;&ndash;&nbsp;Hist�ria de uma fita azul</option>
       <option value=2838 >&nbsp;&ndash;&nbsp;Identidade</option>
       <option value=2839 >&nbsp;&ndash;&nbsp;Jo�o Fernandes</option>
       <option value=2840 >&nbsp;&ndash;&nbsp;Jogo do bicho</option>
       <option value=2841 >&nbsp;&ndash;&nbsp;Letra vencida</option>
       <option value=2842 >&nbsp;&ndash;&nbsp;Longe dos olhos...</option>
       <option value=2843 >&nbsp;&ndash;&nbsp;Mariana (1871)</option>
       <option value=2844 >&nbsp;&ndash;&nbsp;M�dico � rem�dio</option>
       <option value=2845 >&nbsp;&ndash;&nbsp;Miloca</option>
     <option value=2846 >&nbsp;&ndash;&nbsp;Muitos anos depois</option>
     <option value=2847 >&nbsp;&ndash;&nbsp;N�o � o mel para a boca do asno</option>
     <option value=2848 >&nbsp;&ndash;&nbsp;Nem uma nem outra</option>
     <option value=2849 >&nbsp;&ndash;&nbsp;O anjo das donzelas</option>
     <option value=2850 >&nbsp;&ndash;&nbsp;O anjo Rafael</option>
     <option value=2851 >&nbsp;&ndash;&nbsp;O caminho de Damasco</option>
     <option value=2852 >&nbsp;&ndash;&nbsp;O capit�o Mendon�a</option>
     <option value=2853 >&nbsp;&ndash;&nbsp;O carro n�mero 13</option>
     <option value=2854 >&nbsp;&ndash;&nbsp;O caso Barreto</option>
     <option value=2855 >&nbsp;&ndash;&nbsp;O caso da vi�va </option>
     <option value=2856 >&nbsp;&ndash;&nbsp;O caso do Romualdo</option>
     <option value=2857 >&nbsp;&ndash;&nbsp;O contrato</option>
     <option value=2858 >&nbsp;&ndash;&nbsp;O destinado</option>
     <option value=2859 >&nbsp;&ndash;&nbsp;O escriv�o Coimbra</option>
     <option value=2860 >&nbsp;&ndash;&nbsp;O imortal</option>
     <option value=2861 >&nbsp;&ndash;&nbsp;O machete</option>
     <option value=2862 >&nbsp;&ndash;&nbsp;O melhor rem�dio</option>
     <option value=2863 >&nbsp;&ndash;&nbsp;O or�culo</option>
     <option value=2864 >&nbsp;&ndash;&nbsp;O pa�s das Quimeras</option>
     <option value=2865 >&nbsp;&ndash;&nbsp;O passado, passado</option>
     <option value=2866 >&nbsp;&ndash;&nbsp;O programa</option>
     <option value=2867 >&nbsp;&ndash;&nbsp;O que s�o as mo�as</option>
     <option value=2868 >&nbsp;&ndash;&nbsp;O rei dos caiporas</option>
     <option value=2869 >&nbsp;&ndash;&nbsp;O sainete</option>
     <option value=2870 >&nbsp;&ndash;&nbsp;O �ltimo dia de um poeta</option>
     <option value=2871 >&nbsp;&ndash;&nbsp;Onze anos depois</option>
     <option value=2872 >&nbsp;&ndash;&nbsp;Orai por ele!</option>
     <option value=2873 >&nbsp;&ndash;&nbsp;Os �culos de Pedro Ant�o</option>
     <option value=2874 >&nbsp;&ndash;&nbsp;Pobre cardeal!</option>
     <option value=2875 >&nbsp;&ndash;&nbsp;Pobre Finoca!</option>
     <option value=2876 >&nbsp;&ndash;&nbsp;Qual dos dois?</option>
     <option value=2877 >&nbsp;&ndash;&nbsp;Quem conta um conto...</option>
     <option value=2878 >&nbsp;&ndash;&nbsp;Quest�o de vaidade</option>
     <option value=2879 >&nbsp;&ndash;&nbsp;Quest�es de maridos</option>
     <option value=2880 >&nbsp;&ndash;&nbsp;Rui de Le�o</option>
     <option value=2881 >&nbsp;&ndash;&nbsp;Sales</option>
     <option value=2882 >&nbsp;&ndash;&nbsp;Sem olhos</option>
     <option value=2882 >&nbsp;&ndash;&nbsp;Silvestre</option>
     <option value=2884 >&nbsp;&ndash;&nbsp;S�!</option>
     <option value=2885 >&nbsp;&ndash;&nbsp;Tempo de crise</option>
     <option value=2886 >&nbsp;&ndash;&nbsp;Terps�core</option>
     <option value=2887 >&nbsp;&ndash;&nbsp;<i>To be or not to be</i></option>
     <option value=2888 >&nbsp;&ndash;&nbsp;Tr�s conseq��ncias</option>
     <option value=2889 >&nbsp;&ndash;&nbsp;Tr�s tesouros perdidos</option>
     <option value=2890 >&nbsp;&ndash;&nbsp;Trina e una</option>
     <option value=2891 >&nbsp;&ndash;&nbsp;Troca de datas</option>
     <option value=2892 >&nbsp;&ndash;&nbsp;Um almo�o</option>
     <option value=2893 >&nbsp;&ndash;&nbsp;Um ambicioso</option>
     <option value=2894 >&nbsp;&ndash;&nbsp;Um dia de Entrudo</option>
     <option value=2895 >&nbsp;&ndash;&nbsp;Um d�stico</option>
     <option value=2896 >&nbsp;&ndash;&nbsp;Um esqueleto</option>
     <option value=2897 >&nbsp;&ndash;&nbsp;Um homem superior</option>
     <option value=2898 >&nbsp;&ndash;&nbsp;Um inc�ndio</option>
     <option value=2899 >&nbsp;&ndash;&nbsp;Um para o outro</option>
     <option value=28100 >&nbsp;&ndash;&nbsp;Um quarto de s�culo</option>
     <option value=28101 >&nbsp;&ndash;&nbsp;Um sonho e outro sonho</option>
     <option value=28102 >&nbsp;&ndash;&nbsp;Uma �guia sem asas </option>
     <option value=28103 >&nbsp;&ndash;&nbsp;Uma carta</option>
     <option value=28104 >&nbsp;&ndash;&nbsp;Uma excurs�o milagrosa</option>
     <option value=28105 >&nbsp;&ndash;&nbsp;Uma loureira</option>
     <option value=28106 >&nbsp;&ndash;&nbsp;Uma noite</option>
     <option value=28107 >&nbsp;&ndash;&nbsp;Uma partida</option>
     <option value=28108 >&nbsp;&ndash;&nbsp;Uma por outra</option>
     <option value=28109 >&nbsp;&ndash;&nbsp;Val�rio</option>
     <option value=28110 >&nbsp;&ndash;&nbsp;V�nus! Divina V�nus!</option>
     <option value=28111 >&nbsp;&ndash;&nbsp;Viagem � roda de mim mesmo</option>
     <option value=28112 >&nbsp;&ndash;&nbsp;Vidros quebrados</option>
     <option value=28113 >&nbsp;&ndash;&nbsp;Vinte anos! Vinte anos!</option>
     <option value=28114 >&nbsp;&ndash;&nbsp;Virginius</option>
   </select>
   		</div>
			</td>
         <!-- <td class="vazio">&nbsp;</td> -->
          <td class="dots"><img src="figs/form_dots12.gif" width="18" height="18" /></td>
           <td ><div class="pesquisa1">
                <select name="Selcampo" Id="Selcampo1" size="1" onchange="opcao_busca(1)" onkeypress="cbboxSearch(this, event); return false;">
                    <OPTION value= 0  Selected>Selecione
                    <OPTION value= 11 >Autor
                    <OPTION value= 12 >Personagem
                    <OPTION value= 13 >Fonte
                    <OPTION value= 14 >Fato / Per�odo
                    <OPTION value= 0 >Obra citada / mencionada
                    <OPTION value= 151 >&nbsp;&ndash;&nbsp;T�tulo em portugu�s</option>
                    <OPTION value= 152 >&nbsp;&ndash;&nbsp;T�tulo no original</option>
                    <OPTION value= 16 >Lugar
                    <OPTION value= 17 >Trecho da obra ( cont�m )

                    <OPTION value= 31 >Institui��o
                    <OPTION value= 32 >Festividade
                    <OPTION value= 33 >Palavra/Express�o com significado diferente
                    <OPTION value= 34 >Express�o/Palavra em desuso
                    <OPTION value= 35 >Palavra estrangeira
                    <OPTION value= 36 >Express�o estrangeira

                 </select>
			</div>
          </td>
         <!-- <td class="vazio">&nbsp;</td> -->
         </tr>

        </tr>
       <!-- Selecao de Romances -->
         <tr>
          <td class="dots"><img src="figs/form_dots123.gif" width="18" height="18" /></td>
          
             <td><input name="radiobutton" type="radio" class="dots" value="romance" onclick="Hab(2);" /></td>
          
          <td class="formTxL">Romances</td>
          <!-- <td class="vazio">&nbsp;</td> -->
          <td class="dots"><img src="figs/form_dots12.gif" width="18" height="18" /></td>
          <td><div class="pesquisa1">
           <select name="Selromance" size="1" id="Selromance" onkeypress="cbboxSearch(this, event); return false;">
               <OPTION value= 0 Selected>Romances: Selecione --&gt;</option>
               <OPTION value= 10 >Todos os romances
               <option>------------------------------</option>
               <OPTION value= 1 >Ressurrei��o
               <OPTION value= 2 >A m�o e a luva
               <OPTION value= 3 >Helena
               <OPTION value= 4 >Iai� Garcia
               <OPTION value= 5 >Mem�rias p�stumas de Br�s Cubas
               <OPTION value= 6 >Quincas Borba
               <OPTION value= 7 >Dom Casmurro
               <OPTION value= 8 >Esa� e Jac�
               <OPTION value= 9 >Memorial de Aires
            </select>
			</div>
          </td>
        <tr>
          <td class="dots"><img src="figs/form_dots12.gif" width="18" height="18" /></td>

         
              <td><input name="radiobutton" type="radio" class="dots" value="contoromances" onclick="Hab(3);" /></td>
          
          <td class="formTxL">Contos e romances </td>
         <!-- <td class="vazio">&nbsp;</td> -->
        </tr>
      </table>
     </FORM>
     </td>
    </tr>
    <tr>
    <!-- **************************************** -->
     
           <td ><FORM NAME="FORM2" METHOD="Get" ACTION="dtb_resposta_contos_romances.asp">
           <table width="306" border="0" cellpadding="0" cellspacing="0" id="pesquisaForm2">
        
      </table>
      </FORM></td>
    </tr>
  </table>
</div>
<div id="conteudo">
  <table width="756" border="0" cellpadding="0" cellspacing="0" class="conteudoGeral">
    <tr>
      <td class="homeDTB"><p class="tituLanjtx">Banco de dados de cita&ccedil;&otilde;es e alus&otilde;es na fic&ccedil;&atilde;o de Machado de Assis</p>
	  <p class="txBig">
      A base de dados dispon�vel nesta p�gina permite a localiza&ccedil;&atilde;o das cita&ccedil;&otilde;es e alus&otilde;es hist�rico-liter�rias identificadas nos romances e contos de Machado de Assis. Nela, o estudioso interessado em tais cita&ccedil;&otilde;es e alus&otilde;es encontrar� um instrumento de pesquisa que lhe possibilitar� localizar autores citados, assim como obras mencionadas, fatos hist�ricos, personagens (ficcionais ou hist�ricas) e lugares (desde que tenham conota��o alusiva ou simb�lica) nomeados ou a que se faz alus�o. Poder�, ainda, identificar refer�ncias de fontes an�nimas, como prov�rbios, ditados e ad�gios, e cria��es coletivas, como a B�blia, a Mitologia Cl�ssica, ou a Hist�ria.<br />
      S�o identificados tamb�m, a partir de 2017, refer�ncias espaciais como acidentes geogr�ficos, ruas, teatros, igrejas, constela��es; institui��es, como a Escola de Medicina ou a C�mara dos Deputados; festividades tradicionais como o Entrudo ou a Festa do Divino; palavras e express�es que t�m na fic��o de Machado significados diversos dos que t�m hoje; palavras e express�es estrangeiras cujas tradu��es s�o fornecidas ao usu�rio.<br />
      &quot;P&aacute;ginas recolhidas&quot;, &quot;Rel&iacute;quias de casa velha&quot; e &quot;Outros contos&quot;  re&uacute;nem escritos de natureza diversa, neles figurando, ao lado dos contos propriamente ditos, cr�nicas, pe�as de cr�tica, poemas, discursos. S� se incluem aqui refer�ncias dos escritos efetivamente ficcionais desses conjuntos.<br />
      As indica&ccedil;&otilde;es dos cap&iacute;tulos visam possibilitar a f�cil localiza&ccedil;&atilde;o das refer�ncias em qualquer das edi��es da obra do autor.</p>
      <p class="txVerde">Marta de Senna </p>	  </td>
    </tr>
    <tr>
     <td class="rodapeSepara">
        <p class="txVerdeSmall"> <a href="http://machadodeassis.net/dtb_index.asp">CITA&Ccedil;&Otilde;ES E ALUS&Otilde;ES NA FIC&Ccedil;&Atilde;O DE MACHADO DE ASSIS: PESQUISA </a> | <a href="http://machadodeassis.net/dtb_ajuda.asp">AJUDA </a><br />
        <a href="http://machadodeassis.net/hiperTx_romances/index.asp">ROMANCES EM HIPERTEXTO</a> | <a href="http://machadodeassis.net/hiperTx_romances/romances.asp">ROMANCES DISPON&Iacute;VEIS</a> | <a href="http://machadodeassis.net/hiperTx_romances/rht_ajuda.asp">AJUDA</a> <br />
        
        <a href="http://machadodeassis.net/biografia.asp">BIOGRAFIA </a> | <a href="http://machadodeassis.net/biblio.asp">BIBLIOGRAFIA </a> | <a href="http://machadodeassis.net/faq.asp">PERGUNTAS FREQUENTES</a> | <a href="http://machadodeassis.net/links.asp">LINKS</a> | <a href="http://machadodeassis.net/equipe.asp">EQUIPE</a> | <a href="http://machadodeassis.net/contato.asp">CONTATO</a><br />
        <a href="http://machadodeassis.net/index.htm">IN&Iacute;CIO</a>        </p></td>
    </tr>
    <tr>
      <td class="rodapeSepara"><p class="txVerde"><b>www.machadodeassis.net</b><br />
         Base de dados de cita��es e alus�es nos romances e contos de Machado de Assis <br/>

    </tr>

    <tr>
      <td class="rodapeSepara">		<p class="txVerde">&copy; 2007-2009 <br />
        <img src="figs/lg_cnpq.gif" alt="CNPq" width="104" height="45" hspace="80" /><img src="figs/xvazio.gif" width="10" height="10" /><img src="figs/lg_faperj_v03.png" alt="FAPERJ" width="104" height="45" hspace="80" /><img src="figs/xvazio.gif" width="10" height="10" /><img src="figs/lg_casaRui.gif" alt="Fundacao Casa de Rui Barbosa" width="207" height="51" vspace="10" /></p>
</td>
    </tr>

    
  </table>
</div>
</body>

</html>
