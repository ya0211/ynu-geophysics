program test2
    implicit none
    real r,s
    real cal

    write(*,*) 'enter radius'
    read(*,*) r
    s = cal(r)
    write(*,*) s

end program test2

function cal(r)
    implicit none
    real cal,r
    cal = 3.1415*r**2
end function cal