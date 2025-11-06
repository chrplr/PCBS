// JavaScript Document
//
//var StimulGLInfo = new StimulGL_Information();
//var sComponentName = "FirebirdClientPlugin";			
//Log(StimulGLInfo.GetLatestComponentReleaseByName(sComponentName));

function StimulGL_Cleanup()
{
	//window.StimulGLInfo = null;
	StimulGL_CreateArray = null;
}

function StimulGL_CreateArray(length) 
{
	//StimulGL_CreateArray();     // [] or new Array()
	//StimulGL_CreateArray(2);    // new Array(2)
	//StimulGL_CreateArray(3, 2); // [new Array(2),
                    	 //  new Array(2),
                    	 //  new Array(2)]
    var a = new Array(length || 0);
    if (arguments.length > 1) 
	{
        var args = Array.prototype.slice.call(arguments, 1);
        for (var i = 0; i < length; i++) 
		{
            a[i] = StimulGL_CreateArray.apply(this, args);
        }
    }
    return a;
}

///////////////////////////////////////////////////////////
//window.StimulGLInfo = new StimulGL_Information();
function StimulGL_Information()
{
	//alert('StimulGL constructor');
	this.StimulGLReleases = [['2.0.0.2', '4.8.0', '1.0.0.1'], ['2.0.0.3', '4.8.0', '1.0.0.1'], ['2.1.0.0', '5.1.0', '1.0.0.1'], ['2.2.0.0', '5.1.0', '1.0.0.1']];//, ['2.0.0.4', '4.8.0', '1.0.0.1']];
	var PropCounter = 0;
	var AuthorCounter = 0;
	var ComponentCounter = 0;
	var tmpArray;
	var nNumberOfComponentChanges = 0;
	
	this.Doc_FileName_Index = AuthorCounter++;
	this.Doc_Title_Index = AuthorCounter++;
	this.Doc_Version_Index = AuthorCounter++;
	this.Doc_Date_Index = AuthorCounter++;
	this.Doc_Authors_Index = AuthorCounter++;
	
	this.Name_Index = PropCounter++;
	this.Version_Index = PropCounter++;
	this.ProductVersion_Index = PropCounter++;
	this._StimulGLVersion_Index = PropCounter++;
	this.EXML_Index = PropCounter++;
	this.DevInterface_Index = PropCounter++;
	this.ExtInterface_Index = PropCounter++;
	
	var ExperimentManagerPlugin_Comp_Index = ComponentCounter++;
	var ParallelPortPlugin_Comp_Index = ComponentCounter++;
	var SerialPortPlugin_Comp_Index = ComponentCounter++;
	var KeyBoardPlugin_Comp_Index = ComponentCounter++;
	var USBHIDDevicePlugin_Comp_Index = ComponentCounter++;
	var _extensionname_plugin_Comp_Index = ComponentCounter++;
	var StimulGL_QMLExtensions_Comp_Index = ComponentCounter++;
	var MediaPlayer_Comp_Index = ComponentCounter++;
	var FirebirdClientPlugin_Comp_Index = ComponentCounter++;
	var PiezoStimDevicePlugin_Comp_Index = ComponentCounter++;
	var TBVExchangerPlugin_Comp_Index = ComponentCounter++;
	var TCPNetworkServerPlugin_Comp_Index = ComponentCounter++;
	
	this.componentVersioning = StimulGL_CreateArray(1,ComponentCounter,PropCounter);//Default constructor!
	//StimulGL version (2.0.0.2)
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.Name_Index] = 'ExperimentManagerPlugin';
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.Version_Index] = '2.0.0.2';
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this._StimulGLVersion_Index] = 0;
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.EXML_Index] = '2.0.0.1';
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][ExperimentManagerPlugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.Name_Index] = 'ParallelPortPlugin';
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.Version_Index] = '2.0.0.1';
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][ParallelPortPlugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.Name_Index] = 'SerialPortPlugin';
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][SerialPortPlugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.Name_Index] = 'KeyBoardPlugin';
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][KeyBoardPlugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.Name_Index] = 'USBHIDDevicePlugin';
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.Version_Index] = '2.0.0.1';
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][USBHIDDevicePlugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.Name_Index] = '_extensionname_plugin';
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.Version_Index] = '1.0.0.1';
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.DevInterface_Index] = '1.0';
	this.componentVersioning[0][_extensionname_plugin_Comp_Index][this.ExtInterface_Index] = '1.0';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.Name_Index] = 'StimulGL_QMLExtensions';
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.Version_Index] = '1.0';
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.ProductVersion_Index] = 'x';
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.DevInterface_Index] = 'x';
	this.componentVersioning[0][StimulGL_QMLExtensions_Comp_Index][this.ExtInterface_Index] = 'x';
	///////////////////////////////////////////////////////////////
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.Name_Index] = 'MediaPlayer';
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.Version_Index] = '1';
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.ProductVersion_Index] = 'x';
	this.componentVersioning[0][MediaPlayer_Comp_Index][this._StimulGLVersion_Index] = 0; //-->2.0.0.2
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.EXML_Index] = 'x';
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.DevInterface_Index] = 'x';
	this.componentVersioning[0][MediaPlayer_Comp_Index][this.ExtInterface_Index] = 'x';
	///////////////////////////////////////////////////////////////
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.Name_Index] = 'FireBirdClientPlugin';
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this._StimulGLVersion_Index] = 2;
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.EXML_Index] = 'x';
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.DevInterface_Index] = '1.2';
//	this.componentVersioning[0][FirebirdClientPlugin_Comp_Index][this.ExtInterface_Index] = '1.2';	
	///////////////////////////////////////////////////////////////
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.Name_Index] = 'PiezoStimDevicePlugin';
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this._StimulGLVersion_Index] = 2;
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.EXML_Index] = 'x';
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.DevInterface_Index] = '1.2';
//	this.componentVersioning[0][PiezoStimDevicePlugin_Comp_Index][this.ExtInterface_Index] = '1.2';		
	///////////////////////////////////////////////////////////////
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.Name_Index] = 'TBVExchangerPlugin';
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this._StimulGLVersion_Index] = 2;
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.EXML_Index] = 'x';
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.DevInterface_Index] = '1.2';
//	this.componentVersioning[0][TBVExchangerPlugin_Comp_Index][this.ExtInterface_Index] = '1.2';		
	///////////////////////////////////////////////////////////////
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.Name_Index] = 'TCPNetworkServerPlugin';
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.Version_Index] = '1.0.0.1';
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.ProductVersion_Index] = '1.0.0.1';
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this._StimulGLVersion_Index] = 2;
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.EXML_Index] = 'x';
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.DevInterface_Index] = '1.2';
//	this.componentVersioning[0][TCPNetworkServerPlugin_Comp_Index][this.ExtInterface_Index] = '1.2';		
	///////////////////////////////////////////////////////////////
	
		
	//StimulGL version (2.0.0.3)
	///////////////////////////////////////////////////////////////
	nNumberOfComponentChanges = 8;//See below, increment by adding new changes for this release!
	tmpArray = StimulGL_CreateArray(1,nNumberOfComponentChanges,PropCounter);
	this.componentVersioning.push.apply(this.componentVersioning, tmpArray)
	this.componentVersioning[1][ExperimentManagerPlugin_Comp_Index] = 	['ExperimentManagerPlugin',	'2.0.0.3', '1.0.0.1', 1, '2.0.0.2', '1.1',  '1.1'];
	this.componentVersioning[1][ParallelPortPlugin_Comp_Index] =        ['ParallelPortPlugin',      '2.0.0.2', '1.0.0.1', 0, 'x',       '1.1',  '1.1'];
	this.componentVersioning[1][SerialPortPlugin_Comp_Index] =          ['SerialPortPlugin',        '1.0.0.2', '1.0.0.1', 0, 'x',       '1.1',  '1.1'];
	this.componentVersioning[1][KeyBoardPlugin_Comp_Index] =            ['KeyBoardPlugin',          '1.0.0.2', '1.0.0.1', 0, 'x',       '1.1',  '1.1'];
	this.componentVersioning[1][USBHIDDevicePlugin_Comp_Index] =        ['USBHIDDevicePlugin',      '2.0.0.2', '1.0.0.1', 0, 'x',       '1.1',  '1.1'];
	this.componentVersioning[1][_extensionname_plugin_Comp_Index] =     ['_extensionname_plugin',   '1.0.0.2', '1.0.0.1', 0, 'x',       '1.1',  '1.1'];
	this.componentVersioning[1][StimulGL_QMLExtensions_Comp_Index] =    ['StimulGL_QMLExtensions',  '1.1',     '1.0.0.1', 0, 'x',       'x',    'x'];
	this.componentVersioning[1][MediaPlayer_Comp_Index] =               ['MediaPlayer',             '1',       '1.0.0.1', 0, 'x',       'x',    'x'];

	//StimulGL version (2.1.0.0)
	///////////////////////////////////////////////////////////////
	nNumberOfComponentChanges = 8;//See below, increment by adding new changes for this release!
	tmpArray = StimulGL_CreateArray(1,nNumberOfComponentChanges,PropCounter);
	this.componentVersioning.push.apply(this.componentVersioning, tmpArray)//		Name,	Version,  Product, StimGLVersionIndex, EXML, Device, Interface
	this.componentVersioning[2][ExperimentManagerPlugin_Comp_Index] = 	['ExperimentManagerPlugin',	'2.1.0.0', '1.0.0.1', 2, '2.1.0.0', '1.2',  '1.2'];
	this.componentVersioning[2][ParallelPortPlugin_Comp_Index] =        ['ParallelPortPlugin',      '2.0.1.0', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][SerialPortPlugin_Comp_Index] =          ['SerialPortPlugin',        '1.1.0.0', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][KeyBoardPlugin_Comp_Index] =            ['KeyBoardPlugin',          '1.1.0.0', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][USBHIDDevicePlugin_Comp_Index] =        ['USBHIDDevicePlugin',      '2.0.1.0', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][_extensionname_plugin_Comp_Index] =     ['_extensionname_plugin',   '1.1.0.0', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][StimulGL_QMLExtensions_Comp_Index] =    ['StimulGL_QMLExtensions',  '1.1',     '1.0.0.1', 2, 'x',       'x',    'x'];
	this.componentVersioning[2][MediaPlayer_Comp_Index] =               ['MediaPlayer',             '2',       '1.0.0.1', 2, 'x',       'x',    'x'];
	this.componentVersioning[2][FirebirdClientPlugin_Comp_Index] =        ['FireBirdClientPlugin',      '1.0.0.1', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][PiezoStimDevicePlugin_Comp_Index] =        ['PiezoStimDevicePlugin',      '1.0.0.1', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][TBVExchangerPlugin_Comp_Index] =        ['TBVExchangerPlugin',     '1.0.0.1', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];
	this.componentVersioning[2][TCPNetworkServerPlugin_Comp_Index] =        ['TCPNetworkServerPlugin',      '1.0.0.1', '1.0.0.1', 2, 'x',       '1.2',  '1.2'];

	this.DocumentAuditing = StimulGL_CreateArray(14, AuthorCounter); //Default constructor!
	///////////////////////////////////////////////////////////////
	this.DocumentAuditing[0][this.Doc_FileName_Index] = 'GettingStartedGuide.html';
	this.DocumentAuditing[0][this.Doc_Title_Index] = 'Getting Started Guide';
	this.DocumentAuditing[0][this.Doc_Version_Index] = '1.0.1.0';
	this.DocumentAuditing[0][this.Doc_Date_Index] = 'September 2013';
	this.DocumentAuditing[0][this.Doc_Authors_Index] = 'Sven Gijsen';
	
	this.DocumentAuditing[1] = ['PreBuildDevelopmentSetup.html','Pre Build Development Setup','1.0.1.0','September 2013','Sven Gijsen'];
	this.DocumentAuditing[2] = ['ExperimentManagerPlugin.html','Experiment Manager Plug-in Documentation','1.0.1.0','September 2013','Sven Gijsen'];
	this.DocumentAuditing[3] = ['ParallelPortDevicePlugin.html','Parallel Port Plug-in Documentation','2.0.0.2','September 2013','Sven Gijsen'];	
	this.DocumentAuditing[4] = ['USBHIDDevicePlugin.html','USBHID Device Plug-in Documentation','2.0.0.2','September 2013','Sven Gijsen'];		
	this.DocumentAuditing[5] = ['ExtensionPluginTemplate.html','Extension Plug-in Template Documentation','2.0.0.2','September 2013','Sven Gijsen'];	
	this.DocumentAuditing[6] = ['TBVExchangerPlugin.html','Turbo-BrainVoyager Exchanger Plug-in Documentation','1.0.0.1','Oktober 2013','Michael Luehrs'];
	this.DocumentAuditing[7] = ['FireBirdClientPlugin.html','Firebird Client Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];		
	this.DocumentAuditing[8] = ['KeyBoardDevicePlugin.html','Keyboard Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[9] = ['PiezoStimDevicePlugin.html','PiezoStim Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[10] = ['SerialPortDevicePlugin.html','SerialPort Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[11] = ['TCPNetworkServerPlugin.html','TCPNetwork Server Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[12] = ['StimulGL_QMLExtensions.html','StimulGL QML Extensions Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];					
	this.DocumentAuditing[13] = ['6_RetinoTopicMappingOutput.html','Retinotopic Mapping output files Tutorial','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	
	//StimulGL version (2.2.0.0), latest release
	///////////////////////////////////////////////////////////////
	nNumberOfComponentChanges = 8;//See below, increment by adding new changes for this release!
	tmpArray = StimulGL_CreateArray(1,nNumberOfComponentChanges,PropCounter);
	this.componentVersioning.push.apply(this.componentVersioning, tmpArray)//		Name,	Version,  Product, StimGLVersionIndex, EXML, Device, Interface
	this.componentVersioning[3][ExperimentManagerPlugin_Comp_Index] = 	['ExperimentManagerPlugin',	'2.2.0.0', '1.0.0.1', 3, '2.2.0.0', '1.2',  '1.2'];
	this.componentVersioning[3][ParallelPortPlugin_Comp_Index] =        ['ParallelPortPlugin',      '2.1.1.0', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][SerialPortPlugin_Comp_Index] =          ['SerialPortPlugin',        '1.2.0.0', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][KeyBoardPlugin_Comp_Index] =            ['KeyBoardPlugin',          '1.2.0.0', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][USBHIDDevicePlugin_Comp_Index] =        ['USBHIDDevicePlugin',      '2.1.1.0', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][_extensionname_plugin_Comp_Index] =     ['_extensionname_plugin',   '1.2.0.0', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][StimulGL_QMLExtensions_Comp_Index] =    ['StimulGL_QMLExtensions',  '1.2',     '1.0.0.1', 3, 'x',       'x',    'x'];
	this.componentVersioning[3][MediaPlayer_Comp_Index] =               ['MediaPlayer',             '2',       '1.0.0.1', 3, 'x',       'x',    'x'];
	this.componentVersioning[3][FirebirdClientPlugin_Comp_Index] =      ['FireBirdClientPlugin',      '1.1.0.1', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][PiezoStimDevicePlugin_Comp_Index] =     ['PiezoStimDevicePlugin',      '1.1.0.1', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][TBVExchangerPlugin_Comp_Index] =        ['TBVExchangerPlugin',     '1.1.0.1', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];
	this.componentVersioning[3][TCPNetworkServerPlugin_Comp_Index] =    ['TCPNetworkServerPlugin',      '1.1.0.1', '1.0.0.1', 3, 'x',       '1.2',  '1.2'];

	this.DocumentAuditing = StimulGL_CreateArray(15, AuthorCounter); //Default constructor!
	///////////////////////////////////////////////////////////////
	this.DocumentAuditing[0][this.Doc_FileName_Index] = 'GettingStartedGuide.html';
	this.DocumentAuditing[0][this.Doc_Title_Index] = 'Getting Started Guide';
	this.DocumentAuditing[0][this.Doc_Version_Index] = '1.1.1.0';
	this.DocumentAuditing[0][this.Doc_Date_Index] = 'June 2014';
	this.DocumentAuditing[0][this.Doc_Authors_Index] = 'Sven Gijsen';
	
	this.DocumentAuditing[1] = ['PreBuildDevelopmentSetup.html','Pre Build Development Setup','1.0.1.0','September 2013','Sven Gijsen'];
	this.DocumentAuditing[2] = ['ExperimentManagerPlugin.html','Experiment Manager Plug-in Documentation','1.1.1.0','June 2014','Sven Gijsen'];
	this.DocumentAuditing[3] = ['ParallelPortDevicePlugin.html','Parallel Port Plug-in Documentation','2.1.0.2','June 2014','Sven Gijsen'];	
	this.DocumentAuditing[4] = ['USBHIDDevicePlugin.html','USBHID Device Plug-in Documentation','2.0.0.2','September 2013','Sven Gijsen'];		
	this.DocumentAuditing[5] = ['ExtensionPluginTemplate.html','Extension Plug-in Template Documentation','2.0.0.2','September 2013','Sven Gijsen'];	
	this.DocumentAuditing[6] = ['TBVExchangerPlugin.html','Turbo-BrainVoyager Exchanger Plug-in Documentation','1.1.0.1','June 2014','Michael Luehrs'];
	this.DocumentAuditing[7] = ['FireBirdClientPlugin.html','Firebird Client Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];		
	this.DocumentAuditing[8] = ['KeyBoardDevicePlugin.html','Keyboard Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[9] = ['PiezoStimDevicePlugin.html','PiezoStim Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[10] = ['SerialPortDevicePlugin.html','SerialPort Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[11] = ['TCPNetworkServerPlugin.html','TCPNetwork Server Device Plug-in Documentation','1.0.0.1','Oktober 2013','Sven Gijsen'];	
	this.DocumentAuditing[12] = ['StimulGL_QMLExtensions.html','StimulGL QML Extensions Plug-in Documentation','1.1.0.1','June 2014','Sven Gijsen'];					
	this.DocumentAuditing[13] = ['6_RetinoTopicMappingOutput.html','Retinotopic Mapping output files Tutorial','1.1.0.1','June 2014','Sven Gijsen'];	
	this.DocumentAuditing[14] = ['15_NeuroFeedBack.html','NeuroFeedback Tutorial (with TBVExchanger plugin)','1.1.0.1','June 2014','Sven Gijsen'];
}

StimulGL_Information.prototype.GetStrippedFileName = function (strFileUrl)//var strFileUrl=window.location.pathname;
{
	return strFileUrl.replace(/^.*[\\\/]/, '');
}

StimulGL_Information.prototype.GetDocumentIndex = function (strFileUrl)//var strFileUrl=window.location.pathname;
{
	//alert('GetDocumentIndex ' + strFileUrl);
	if ((strFileUrl===undefined) || (strFileUrl==''))
		return -1;
	var filename = this.GetStrippedFileName(strFileUrl)
	var nDocuments = this.DocumentAuditing.length;
	for (var i=0;i<nDocuments;i++) 
	{
		if(this.DocumentAuditing[i][this.Doc_FileName_Index] == filename)
		{
			//alert('found it! -> ' + filename);
			return i;
		}
	}
	//alert('not found it... -> ' + filename);
	return -1;
}

StimulGL_Information.prototype.GetDocumentTitle = function (strFileUrl)
{
	//alert('GetDocumentTitle');
	var nDocIndex = this.GetDocumentIndex(strFileUrl);
	if(nDocIndex >= 0)
		return this.DocumentAuditing[nDocIndex][this.Doc_Title_Index];
	return this.GetStrippedFileName(strFileUrl);
}

StimulGL_Information.prototype.GetDocumentHeader = function (strFileUrl)
{
	//alert('GetDocumentHeader ' + strFileUrl);
	var nDocIndex = this.GetDocumentIndex(strFileUrl);
	//alert('GetDocumentHeader ' + nDocIndex);
	if(nDocIndex >= 0)
	{
		document.write('<h1>' + this.DocumentAuditing[nDocIndex][this.Doc_Title_Index] + '</h1>');
		document.write('<p><em><strong>Version ' + this.DocumentAuditing[nDocIndex][this.Doc_Version_Index] + '</strong></em></p>'); //+ ', for StimulGL v' + + '</p>');
		document.write('<p><em><strong>' + this.DocumentAuditing[nDocIndex][this.Doc_Date_Index] + ', by ' + this.DocumentAuditing[nDocIndex][this.Doc_Authors_Index] + '</strong></em></p>');
	}
	else
	{
		document.write('<h1>' + this.GetStrippedFileName(strFileUrl) + '</h1>');
	}
	document.write('<p>&nbsp;</p>');
}

StimulGL_Information.prototype.GetCurrentRelease = function ()
{
	//alert('GetCurrentRelease');
	return this.StimulGLReleases[this.StimulGLReleases.length-1][0];
}

StimulGL_Information.prototype.GetReleaseByIndex = function (nIndex)
{
	//alert('GetReleaseByIndex');
	return this.StimulGLReleases[nIndex][0];
}

StimulGL_Information.prototype.GetReleaseQtVersionByIndex = function (nIndex)
{
	//alert('GetReleaseQtVersionByIndex');
	return this.StimulGLReleases[nIndex][1];
}

StimulGL_Information.prototype.GetReleaseProductVersionByIndex = function (nIndex) {
    //alert('GetReleaseProductVersionByIndex');
    return this.StimulGLReleases[nIndex][2];
}

StimulGL_Information.prototype.GetNumberOfReleases = function ()
{
	//alert('GetNumberOfReleases');
	return this.StimulGLReleases.length;
}

StimulGL_Information.prototype.GetNumberOfComponentsByReleaseIndex = function (nReleaseIndex)
{
	//alert('GetComponentRelease ' + nReleaseIndex);
	if(this.componentVersioning.length > nReleaseIndex)
	{
		return this.componentVersioning[nReleaseIndex].length;
	}
	return 0;
}

StimulGL_Information.prototype.CheckComponentByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('CheckComponentByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.componentVersioning.length > nReleaseIndex)
	{
		if(this.componentVersioning[nReleaseIndex].length > nComponentIndex)
		{		
			return true;
		}
	}
	return false;
}

StimulGL_Information.prototype.GetLatestComponentReleaseByName = function (strComponentName)
{
	//alert('GetLatestComponentReleaseByName ' + strComponentName);
	for(var i=this.componentVersioning.length-1;i>=0;i--)
	{
		for(var j=0;j<this.componentVersioning[i].length;j++)
		{
		    if (this.componentVersioning[i][j][this.Name_Index] == strComponentName)
			{		
				return i;
			}
		}
	}	
	return -1;
}

StimulGL_Information.prototype.GetLatestComponentIndexByName = function (nReleaseIndex, strComponentName)
{
	//alert('GetLatestComponentIndexByName ' + strComponentName);
	for(var j=0;j<this.componentVersioning[nReleaseIndex].length;j++)
	{
	    if (this.componentVersioning[nReleaseIndex][j][this.Name_Index] == strComponentName)
		{		
			return j;
		}
	}	
	return -1;
}

StimulGL_Information.prototype.GetComponentNameByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentNameByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
		return this.componentVersioning[nReleaseIndex][nComponentIndex][this.Name_Index];
	return '';
}

StimulGL_Information.prototype.GetComponentStimGLVersionByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentStimGLVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
	{
		return this.StimulGLReleases[this.componentVersioning[nReleaseIndex][nComponentIndex][this._StimulGLVersion_Index]][0];
	}
	return '';
}

StimulGL_Information.prototype.GetComponentVersionByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
		return this.componentVersioning[nReleaseIndex][nComponentIndex][this.Version_Index];
	return '';
}

StimulGL_Information.prototype.GetComponentProductVersionByIndexes = function (nReleaseIndex, nComponentIndex) {
    //alert('GetComponentProductVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
    if (this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
        return this.componentVersioning[nReleaseIndex][nComponentIndex][this.ProductVersion_Index];
    return '';
}

StimulGL_Information.prototype.GetComponentMinimalEXMLVersionByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentMinimalEXMLVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
		return this.componentVersioning[nReleaseIndex][nComponentIndex][this.EXML_Index];
	return '';
}

StimulGL_Information.prototype.GetComponentDeviceInterfaceVersionByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentDeviceInterfaceVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
		return this.componentVersioning[nReleaseIndex][nComponentIndex][this.DevInterface_Index];
	return '';
}

StimulGL_Information.prototype.GetComponentExtensionInterfaceVersionByIndexes = function (nReleaseIndex, nComponentIndex)
{
	//alert('GetComponentExtensionInterfaceVersionByIndexes ' + nReleaseIndex + ", " + nComponentIndex);
	if(this.CheckComponentByIndexes(nReleaseIndex, nComponentIndex))
		return this.componentVersioning[nReleaseIndex][nComponentIndex][this.ExtInterface_Index];
	return '';
}

StimulGL_Information.prototype.GetMainAppCopyrightString = function ()
{ return 'Copyright (C) 2014'; }

StimulGL_Information.prototype.GetMainAppCompanyName = function ()
{	return 'MBIC, Maastricht Brain Imaging Center'; }

StimulGL_Information.prototype.GetMainAppInternalName = function ()
{	return 'StimulGL'; }

StimulGL_Information.prototype.GetMainAppPluginDeviceInterfaceString = function ()
{	return 'StimulGL.Plugins.DeviceInterface/1.2'; }

StimulGL_Information.prototype.GetMainAppPluginExtensionInterfaceString = function ()
{	return 'StimulGL.Plugins.ExtensionInterface/1.2'; }
