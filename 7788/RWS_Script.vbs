sub main
  crt.Screen.Synchronous =true 
  crt.Screen.Send "manage" & chr(13)
 

  crt.Screen.WaitForString "Please verify your identity(Enter)"
  crt.Screen.Send chr(13)

  
  
  crt.Screen.WaitForString "Please input passwd:"
  crt.Screen.Send "12345678" & chr(13)
 
  
  
  crt.Screen.WaitForString "localhost(management)#"
  crt.Screen.Send "rootprivilege" & chr(13)
  

  
  crt.Screen.WaitForString "localhost(privilege)#"
  crt.Screen.Send "_admin_shell_" & chr(13)
  
  
  
  crt.Screen.WaitForString "Please input passwd:"
  crt.Screen.Send "_fdaCVIbew$%^&*vcmzCnv+m_" & chr(13)
end sub