document.getElementById("postform").addEventListener('submit',(e)=>{
    e.preventDefault();
    const form = document.getElementById("postform");
    const fd = new FormData(form);
    console.log(fd)
    fetch(`http://127.0.0.1:8000/student/`,{
        method:"POST",
        body:fd
    }).then((res)=>{return res.json()}).then((data)=>console.log(data)).catch(err=>document.getElementById("main").innerHTML=err)
})
document.getElementById("getform").addEventListener('submit',(e)=>{
document.getElementById("cnt1").innerHTML=""
document.getElementById("cnt2").innerHTML=""
document.getElementById("cnt3").innerHTML=""
document.getElementById("cnt4").innerHTML=""
    e.preventDefault();
    const form = document.getElementById("getform");
    const fd = new FormData(form);
    const obj1=Object.fromEntries(fd);
    // console.log(obj1.id)
    if(obj1.id !='')
    {fetch(`http://127.0.0.1:8000/student/${obj1.id}`).then(val=>val.json()).then(data=>{
        
            // document.getElementById("main").innerText+=data.id+".----"+data.name+"-----"+data.roll+"-----"+data.subject+"<br/>";
            document.getElementById("cnt1").innerHTML+=data.id;
            document.getElementById("cnt2").innerHTML+=data.name;
            document.getElementById("cnt3").innerHTML+=data.roll;
            document.getElementById("cnt4").innerHTML+=data.subject;

    })}
    else{
        fetch(`http://127.0.0.1:8000/student/`).then(val=>val.json()).then(data=>{
        if (typeof(data)=="object")
        // console.log(data)
        data.map((item)=>{
            // document.getElementById("main").innerHTML+=item.id+".----"+item.name+"-----"+item.roll+"-----"+item.subject+"<br/>";
            document.getElementById("cnt1").innerHTML+=item.id+"<br/>";
            document.getElementById("cnt2").innerHTML+=item.name+"<br/>";
            document.getElementById("cnt3").innerHTML+=item.roll+"<br/>";
            document.getElementById("cnt4").innerHTML+=item.subject+"<br/>";


        })
    })
    }
});