async function login(email: string, password: string) {
    const userData: FormData = new FormData();
    userData.append('username', email);
    userData.append('password', password);

    let requestData: object = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${email}&password=${password}`,
    }

    let responseData = await fetch("/fapi/v1/authorization/token", requestData);

    if (responseData.ok == false) {
        throw Error("Неверный логин или пароль");
    }

    let result = await responseData.json();

    return result.access_token;
}

export default login;