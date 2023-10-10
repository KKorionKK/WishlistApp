<script>
    import TextButton from "./buttons/TextButton.svelte";
    import AccentButton from "./buttons/AccentButton.svelte";
</script>

<div class="header-div">
    <span class="header-span">Wishlists</span>
    <div class="nav-btns">
        <TextButton name="Home"></TextButton>
        <TextButton name="About"></TextButton>
    </div>
    <div class="auth-btns">
        <AccentButton name="Register"></AccentButton>
        <AccentButton name="Login"></AccentButton>
    </div>
</div>

<style>
    .header-div {
        display: flex;
        flex-direction: row;
        position: fixed;
        top: 0px;
        left: 0px;
        width: 100%;
        border-bottom: rgb(176, 176, 176) solid 1px;
        padding-bottom: 20px;
        padding-top: 20px;
        z-index: 1000;
        backdrop-filter: blur(10px);
    }
    .header-span {
        font-weight: 800;
        color: #FF6B3D;
        font-size: 28px;
        flex: 1;
        user-select: none;
    }
    .nav-btns {
        justify-content: center;
        display: flex;
        flex-direction: row;
        flex: 2;
    }
    .auth-btns {
        justify-content: center;
        display: flex;
        flex-direction: row;
        align-items: center;
        flex: 1;
    }
</style>