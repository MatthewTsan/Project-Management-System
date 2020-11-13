/**
说明：
引入js文件：<script src="script_check.js" type="text/javascript"></script>
<input id="username" type="text" name="users" maxlength=8  onkeyup="checkRate(this.id)" >
 */
 
 /*
function checkRate(input)
{
    var re = /^[0-9]+.?[0-9]*$/;  //判断字符串是否为数字   
    var nubmer = document.getElementById(input).value;
    
     if (!re.test(nubmer))
     {
        alert("请输入数字");
        document.getElementById(input).value = "";
        return false;
     }
}*/

//验证表单信息有效性的函数	
 function checkform()
 {
	 var reader_no=document.formZC.reader_no;
	 var pwd=document.formZC.pwd;
	 var repwd=document.formZC.repwd;
	 var name=document.formZC.name;
	 var tel=document.formZC.tel;
	 

     //调用checkLength()函数判断长度
     if(checkLength(reader_no,8))  
     {
		alert("必须输入为8位数字作为读者编号!");
		document.formZC.reader_no.focus();
		return false;
     }
     if(isNum(reader_no))  
     {
		alert("必须输入为8位数字作为读者编号!");
		document.formZC.reader_no.focus();
		return false;
     }
     
	 //调用isempty()函数判断输入是否为空
	 if(isempty(pwd))   
      {alert("密码不能为空，请输入密码!"); 
       document.formZC.pwd.focus();
       return false;
      }
	 
	  //判断二次输入的密码是否一致
	  if(repwd.value!=pwd.value)
	  {
		alert("两次输入的密码不一致！");
		document.formZC.repwd.focus() ;
		return false;
     }
	 
	  
      //调用isChinese()函数判断姓名输入是否为汉字
	 if(isempty(name))
      {
		alert("姓名不能为空且必须为汉字！");
		document.formZC.name.focus() ;
		return false;
      }
	 if(isChinese(name))
     {
		alert("姓名不能为空且必须为汉字！");
		document.formZC.name.focus() ;
		return false;
     }
	  
	  //调用isTel()函数判断电话号码格式是否正确
	 if(isempty(tel))
	  {
		alert("电话号码不能为空，请重新输入!") ;
		document.formZC.tel.focus()  ;
		return false;
	  }
/*	 if(isTel(tel))
	  {
		alert("电话号码格式不正确，请重新输入!") ;
		document.formZC.tel.focus()  ;
		return false;
	  }
*/
}

//判断是否为电话号码
function isTel(object) 
	{ 
		var i,j,strTemp; 
		strTemp = "0123456789- ()"; 
		for (i=0;i<object.length;i++) 
		{ 
			j = strTemp.indexOf(object.charAt(i)); 
			if (j==-1) 
			{ 
				//说明有字符不合法 
				return true; 
			} 
		} 
		//说明合法 
		return false; 
	} 

//检验输入是否为数字
function isNum(object)   
 {
   var inputstr=object.value.toString();
   var length=inputstr.length;
   if (length>0)
     {for(var i=0;i<inputstr.length;i++)
      {  
       var onechar=inputstr.charAt(i);
       if(onechar<"0" || onechar>"9" )
       {
         return true;
        }
       }
       return false;
      } 
   else
     return false;     
 }   
	
//判断对象值是否为空
function isempty(object)  
  { 
    var str = object.value;
    if (str==null || str=="")
       return true;
    else 
       return false;
   }

//检验字符串长度
function checkLength(object,n)
{ if(object.length==0)
 return false;
if(object.value.length==n)
  return false;
else
  return true;
}

//检测输入是否为中文
function isChinese(object) 
{
var i;
   for(i=0;i<object.value.length;i++)
  {
  if(object.value.charCodeAt(i)>=32&&object.value.charCodeAt(i)<=128)
  return true;
  }
return false;
}