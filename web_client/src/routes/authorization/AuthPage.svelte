<form method="POST" class="authBox">
    <fieldset>
        <label for="email">Email</label>
        <input name="email" type="text">
    </fieldset>
    <input class="inputMeow" name="password" type="password" placeholder="Your datebirth? ^.^">
<div class="formBtns">
    <input class="btnMeow" style="background: #E6E2CC;" type="button" on:click={attemptToLogin} value="Login">
    <input class="btnMeow" style="background: #C1BEAC;" type="button" on:click={register} value="Register">
</div>
</form>

<script lang="ts">
    import login from "../../lib/login";
    async function register() {
        window.location.href = "/register";
    }
    async function attemptToLogin() {
        let elements: NodeListOf<Element> = document.querySelectorAll(".authBox input.inputMeow")
        const email: string = elements[0].value;
        const password: string = elements[1].value;
        

        let result = await login(email, password);

        localStorage.setItem('access_token', result.access_token);
        
        window.location.href = "/profile";
    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@200&family=Open+Sans:wght@300;400;500;700;800&display=swap');
    * {
        font-family: 'Open Sans', sans-serif;
    }
    .authBox {
        position: relative;
        margin: auto;
        background-color: #FF6B3D;
        border: solid 1px black;
        border-radius: 38px;
        display: flex;
        flex-direction: column;
        padding: 50px;
    }
   
</style>