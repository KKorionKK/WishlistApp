<form method="POST" class="authBox">
    <div class="field">
        <label for="email">Email</label>
        <input class="inputMeow" name="email" type="email" required>
    </div>
    <input class="inputMeow" name="name" type="text" required>
    <input class="inputMeow" name="nickname" type="text" required>
    <input class="inputMeow" name="birthday" type="date" required>
    <input class="inputMeow" name="password" type="password" required>
    <input class="inputMeow" name="gender" type="checkbox">
    <input class="inputMeow" name="zodiac" type="tel">
    <input class="btnMeow" style="background: #E6E2CC;" type="button" on:click={attemptToRegister} value="Register">
</form>

<script lang="ts">
    async function attemptToRegister() {
        
    }

</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@200&family=Open+Sans:wght@300;400;500;700;800&display=swap');
    * {
        font-family: 'Open Sans', sans-serif;
        color: rgb(122, 122, 122);
    }
    .field {
        position:relative;
        display: flex;
        flex-direction: column;
    }
    label {
        color:rgb(172, 167, 167);
        font-weight:600;
        position:relative;
        width: fit-content;
        pointer-events:none;
        transition:0.2s ease all; 
        -moz-transition:0.2s ease all; 
        -webkit-transition:0.2s ease all;
    }
    .authBox {
        position: relative;
        margin: auto;
        background-color: #FFFBE3;
        border: solid 1px black;
        border-radius: 38px;
        display: flex;
        flex-direction: column;
        padding: 50px;
    }
    .inputMeow {
        font-weight: 500;
        border: solid 1px #000000;
        border-radius: 15px;
        background-color: #FFFBE3;
        padding: 20px;
        width: 450px;
        margin-bottom: 30px;
        letter-spacing: 2px;
    }
    .btnMeow {
        color: white;
        padding: 20px;
        border-radius: 38px;
        border: 1px solid #000;
        font-weight: 800;
        line-height: normal;
        letter-spacing: 6.48px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .btnMeow:hover {
        font-size: 12px;
        padding: 15px;
    }
</style>