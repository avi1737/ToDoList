document.getElementById("addInvoice").addEventListener("click",function(){
document.querySelector(".content").innerHTML="";    
document.querySelector(".content").appendChild(InvoiceFormContainer);
});

document.getElementById("showInvoice").addEventListener("click",function(){
    document.querySelector(".content").innerHTML="";
    document.querySelector(".content").appendChild(invoiceTable);
});


//code for form container of invoice
var InvoiceFormContainer=document.createElement("div");
var AddInvoiceText=document.createElement("h1");
var Invoiceform=document.createElement("form");
var InvoiceId=document.createElement("input");
var InvoiceAmount=document.createElement("input");
var InvoiceDate=document.createElement("input");
var InvoiceNo=document.createElement("input");
var InvoicePaid=document.createElement("input");
var InvoiceTM=document.createElement("input");
var InvoiceDateAdded=document.createElement("input");
var CuCode=document.createElement("input");
var Customer=document.createElement("input");

var documentFragment=document.createDocumentFragment();
documentFragment.appendChild(Invoiceform);
Invoiceform.appendChild(InvoiceId);
Invoiceform.appendChild(InvoiceAmount);
Invoiceform.appendChild(InvoiceDate);
Invoiceform.appendChild(InvoiceNo);
Invoiceform.appendChild(InvoicePaid);
Invoiceform.appendChild(InvoiceTM);
Invoiceform.appendChild(InvoiceDateAdded);
Invoiceform.appendChild(CuCode);
Invoiceform.appendChild(Customer);
InvoiceFormContainer.appendChild(AddInvoiceText);

InvoiceFormContainer.appendChild(documentFragment);
var InputInArray=Invoiceform.children;
for(let j=0;j<InputInArray.length;j++){
    InputInArray[j].classList.add("input");
}
InvoiceId.setAttribute("type","text");
InvoiceId.setAttribute("placeholder","Invoice Id.");
InvoiceAmount.setAttribute("type","text");
InvoiceAmount.setAttribute("placeholder","Invoice Amount");
InvoiceDate.setAttribute("type","date");
InvoiceDate.setAttribute("placeholder","Invoice date");
InvoiceNo.setAttribute("type","text");
InvoiceNo.setAttribute("placeholder","Invoice Id.");
InvoicePaid.setAttribute("type","text");
InvoicePaid.setAttribute("placeholder","Invoice paid");
InvoiceTM.setAttribute("type","text");
InvoiceTM.setAttribute("placeholder","Invoice tm");
InvoiceDateAdded.setAttribute("type","date");
InvoiceDateAdded.setAttribute("placeholder","Invoice date added");
CuCode.setAttribute("type","text");
CuCode.setAttribute("placeholder","Enter Cucode");
Customer.setAttribute("type","text");
Customer.setAttribute("placeholder","customer");

//code for table of invoice






