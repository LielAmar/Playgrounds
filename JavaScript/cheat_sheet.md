# JavaScript Cheat Sheet

## NVM

- List Node versions `nvm list`
- Use Node version `nvm use <node_version>`
- Add Node version `nvm install <node_version>`

## NPM

- Initialize a project `npm init [-y]`
- Install package `npm install [--save-dev] <package>`
- Uninstall package `npm uninstall <package>`
- Run a script `npm run <script>`
- Add a script

```json
"scripts": {
  "start": "tsc index.ts && node index.js",
}
```

## NextJS

- Initialize a project `npx create-next-app@latest`
- Run development environment `npm run dev`
- Build application `npm run build`
