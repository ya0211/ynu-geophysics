program test2
  implicit none
  character(30) :: string
  character(30) remove_spaces

  write(*,*) "Enter a string (use quotation marks)"
  read(*,*)string
  !write(*,*) "string = '", string, "'"

  string = remove_spaces(string)
  write(*,*) "string = '", trim(string), "'"

end program test2

function remove_spaces(in_str)
  character(30) remove_spaces
  character(*), intent(in) :: in_str
  character(30) :: out_str
  character :: ch
  integer :: j

  out_str = " "
  do j = 1,len_trim(in_str)
     ch = in_str(j:j)
     if (ch .ne. " ") then
        out_str = trim(out_str) // ch
     endif
     remove_spaces = out_str 
  end do
end function remove_spaces