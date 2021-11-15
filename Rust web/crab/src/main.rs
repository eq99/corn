mod entity;

use entity::{users, users::Entity as Users};
use sea_orm::{prelude::*, ActiveValue, Database, Set, Unset};
use std::env;
use tera::Tera;
use tide::prelude::*;
use tide::{Request,Response};
use tide_tera::prelude::*;

#[async_std::main]
async fn main() -> tide::Result<()> {
    tide::log::start();
    let tera = Tera::new("templates/**/*")?;

    let mut app = tide::with_state(tera);
    app.at("/").get(home);
    app.at("/users").post(create_user);
    app.at("/public").serve_dir("public/")?;
    app.listen("127.0.0.1:8080").await?;
    Ok(())
}

async fn create_user(mut req: Request<(Tera)>) -> tide::Result {
    let user = req.body_json().await?;
    println!("{:?}", user);
    tide::Response::new(200).body_json(&user)?
}

async fn home(req: Request<Tera>) -> tide::Result {
    let tera = req.state();
    let hello = "你好";
    tera.render_response("home.html", &context! { "hello" => hello })
}
