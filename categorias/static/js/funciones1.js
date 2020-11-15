$(document).ready(function()
{ 
  $('#cat1').hover(function()
  {
     $('#lista1').slideDown();
     $('#lista2').slideUp();
     $('#lista3').slideUp();
     $('#lista4').slideUp();
     $('#lista5').slideUp();
     $('#lista6').slideUp();
  });

  $('#lista1').mouseleave(function()
  {
     $('#lista1').slideUp();
     
  });

  $('#cat2').hover(function()
  {
     $('#lista2').slideDown();
     $('#lista1').slideUp();
     $('#lista3').slideUp();
     $('#lista4').slideUp();
     $('#lista5').slideUp();
     $('#lista6').slideUp();
  });

  $('#lista2').mouseleave(function()
  {
     $('#lista2').slideUp();
  });

  $('#cat3').hover(function()
  {
     $('#lista3').slideDown();
     $('#lista2').slideUp();
     $('#lista1').slideUp();
     $('#lista4').slideUp();
     $('#lista5').slideUp();
     $('#lista6').slideUp();
  });

  $('#lista3').mouseleave(function()
  {
     $('#lista3').slideUp();
  });

  $('#cat4').hover(function()
  {
     $('#lista4').slideDown()
     $('#lista2').slideUp();
     $('#lista3').slideUp();
     $('#lista1').slideUp();
     $('#lista5').slideUp();
     $('#lista6').slideUp();;
  });

  $('#lista4').mouseleave(function()
  {
     $('#lista4').slideUp();
  });

  $('#cat5').hover(function()
  {
     $('#lista5').slideDown();
     $('#lista2').slideUp();
     $('#lista3').slideUp();
     $('#lista4').slideUp();
     $('#lista1').slideUp();
     $('#lista6').slideUp();
  });

  $('#lista5').mouseleave(function()
  {
     $('#lista5').slideUp();
  });

  $('#cat6').hover(function()
  {
     $('#lista6').slideDown();
     $('#lista2').slideUp();
     $('#lista3').slideUp();
     $('#lista4').slideUp();
     $('#lista5').slideUp();
     $('#lista1').slideUp();
  });

  $('#lista6').mouseleave(function()
  {
     $('#lista6').slideUp();
  });


});




