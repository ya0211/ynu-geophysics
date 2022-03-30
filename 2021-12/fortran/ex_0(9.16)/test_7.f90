program e7
implicit none
integer::a(5) = (/ 1,2,3,4,5 /)
call ShowOne(a)
call ShowArray3(a)
call ShowArray5(a)
call ShowArray3(a(2)) 
call ShowArray2X2(a)
stop
end

subroutine ShowOne(num)
implicit none
integer :: num(5)
write(*,*) num(5)
return
end

subroutine ShowArray5(num)
implicit none
integer::num(5)
write(*,*) num
return
end

subroutine ShowArray3(num)
implicit none
integer :: num(3)
write(*,*) num
return
end

subroutine ShowArray2X2(num)
implicit none
integer :: num(2,2)
write(*,*) num(2,1), num(2,2)
return
end