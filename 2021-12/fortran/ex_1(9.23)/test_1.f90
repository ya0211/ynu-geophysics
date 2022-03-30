program test1
    implicit none
    real a
    real b

    write(*,*)"Enter monthly income"
    read(*,*)a
    
    if(a<1000)then
        b=a*0.03
    else if(a>5000)then
        b=a*0.15
    else
        b=a*0.1
    endif
    write(*,*)"Tax payable",b
    !write(*,*)b
    
end