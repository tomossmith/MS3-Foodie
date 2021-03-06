// FUNCTION TO INITIATE THE SIDE NAVIGATION BAR AND DROPDOWN
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $(".dropdown-trigger").dropdown();
  });

// FUNCTION TO RUN SELECT FIELD ON FORMS
$(document).ready(function(){
  $('select').formSelect();
});

// FUNCTION TO ADD CHARACTER COUNT TO SOME INPUT FIELDS ON FORMS
$(document).ready(function() {
  $('input#recipe_name, textarea#recipe_description').characterCounter();
});

// ADD INGREDIENT FUNCTION ON THE ADD RECIPE FORM
// CREDIT: https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/

//Ingredients
$(document).ready(function(){
  var ingredientMaxField = 30; //Input fields increment limitation
  var ingredientAddButton = $('.ingredient_add_button'); //Add button selector
  var ingredientWrapper = $('.ingredient_field_wrapper'); //Input field wrapper
  var ingredientFieldHTML = '<div class="ingredient_field_wrapper input-field"><input id="recipe_ingredients" name="recipe_ingredients" type="text" minlength="3"><label for="recipe_ingredients">Next Ingredient</label><a href="javascript:void(0);" class="ingredient_remove_button"><p><i class="fas fa-trash-alt"></i> Remove Ingredient</p></a></div>'; //New input field html 
  var x = 1; //Initial field counter is 1
  
  //Once add button is clicked
  $(ingredientAddButton).click(function(){
      //Check maximum number of input fields
      if(x < ingredientMaxField){ 
          x++; //Increment field counter
          $(ingredientWrapper).append(ingredientFieldHTML); //Add field html
      }
  });
  
  //Once remove button is clicked
  $(ingredientWrapper).on('click', '.ingredient_remove_button', function(e){
      e.preventDefault();
      $(this).parent('div').remove(); //Remove field html
      x--; //Decrement field counter
  });
});

//Instruction
$(document).ready(function(){
  var instructionMaxField = 30; //Input fields increment limitation
  var instructionAddButton = $('.instruction_add_button'); //Add button selector
  var instructionWrapper = $('.instruction_field_wrapper'); //Input field wrapper
  var instructionFieldHTML = '<div class="instruction_field_wrapper input-field"><input id="recipe_instructions" name="recipe_instructions" type="text" minlength="3"><label for="recipe_instructions"> Next Instruction</label><a href="javascript:void(0);" class="instruction_remove_button"><p><i class="fas fa-trash-alt"></i> Remove Instruction</p></a></div>'; //New input field html 
  var x = 1; //Initial field counter is 1
  
  //Once add button is clicked
  $(instructionAddButton).click(function(){
      //Check maximum number of input fields
      if(x < instructionMaxField){ 
          x++; //Increment field counter
          $(instructionWrapper).append(instructionFieldHTML); //Add field html
      }
  });
  
  //Once remove button is clicked
  $(instructionWrapper).on('click', '.instruction_remove_button', function(e){
      e.preventDefault();
      $(this).parent('div').remove(); //Remove field html
      x--; //Decrement field counter
  });
});  