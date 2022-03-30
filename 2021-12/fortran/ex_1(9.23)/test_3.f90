program test3
    implicit none
    integer age
    real num
    real b

    write(*,*)"Enter age"
    read(*,*)age
    write(*,*)"Enter monthly income"
    read(*,*)num

    if(age<50)then
        if(num<1000)then
            b=num*0.03
        else if(num>5000)then
            b=num*0.15
        else
            b=num*0.1
        endif
    else
        if(num<1000)then
            b=num*0.05
        else if(num>5000)then
            b=num*0.1
        else
            b=num*0.07
        endif
    endif
    write(*,*)"Tax payable"
    write(*,*)b

end