##os related commands
mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS=false\n\
headless=true\n\
\n\
">~/.streamlit/credentials.toml