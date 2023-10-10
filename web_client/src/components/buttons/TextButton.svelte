<script lang="ts">
    export let name: string;
</script>

<input type="button" value={name} class="text-btn">

<style>
    .text-btn {
        margin-inline: 20px;
        font-weight: 300;
        font-size: 16px;
        border: none;
        background: none;
        cursor: pointer;
        color: #FF6B3D;
    }
</style>