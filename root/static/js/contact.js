

document.getElementById('showSignup').addEventListener('click',function(){
        document.getElementById('loginForm').style.display="none";
        document.getElementById('signupForm').style.display="block";
    }
);

document.getElementById('showLogin').addEventListener('click',function(){
        document.getElementById('signupForm').style.display="none";
        document.getElementById('loginForm').style.display="block";
    }
);
