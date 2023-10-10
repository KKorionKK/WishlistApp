<script lang="ts">
    export let name: string;
</script>

<input type="button" value={name} class="accent-btn">

<style>
    .accent-btn {
        font-weight: 600;
        font-size: 12px;
        height: 30px;
        width: 100px;
        border: 0;
        border-radius: 10px;
        background-color: #FF6B3D;
        cursor: pointer;
        color: white;
    }
</style>