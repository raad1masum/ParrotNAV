function copyJsAndCordovaLib (projectPath, projectName, use_shared, config) {
    fs.copySync(path.join(ROOT, 'CordovaLib', 'cordova.js'), path.join(projectPath, 'www/cordova.js'));
    fs.copySync(path.join(ROOT, 'cordova-js-src'), path.join(projectPath, 'platform_www/cordova-js-src'));
    fs.copySync(path.join(ROOT, 'CordovaLib', 'cordova.js'), path.join(projectPath, 'platform_www/cordova.js'));

    /*
     * Check if "CordovaLib" already exists with "fs.lstatSync" and remove it.
     * Wrapped with try/catch because lstatSync will throw an error if "CordovaLib"
     * is missing.
     */
    try {
        const stats = fs.lstatSync(path.join(projectPath, 'CordovaLib'));
        if (stats.isSymbolicLink()) {
            fs.unlinkSync(path.join(projectPath, 'CordovaLib'));
        } else {
            fs.removeSync(path.join(projectPath, 'CordovaLib'));
        }
    } catch (e) { }
    if (use_shared) {
        update_cordova_subproject([path.join(projectPath, `${projectName}.xcodeproj`, 'project.pbxproj'), config]);
        // Symlink not used in project file, but is currently required for plugman because
        // it reads the VERSION file from it (instead of using the cordova/version script
        // like it should).
        fs.symlinkSync(path.join(ROOT, 'CordovaLib'), path.join(projectPath, 'CordovaLib'));
    } else {
        const r = path.join(projectPath, projectName);
        fs.ensureDirSync(path.join(projectPath, 'CordovaLib', 'CordovaLib.xcodeproj'));
        fs.copySync(path.join(r, '.gitignore'), path.join(projectPath, '.gitignore'));
        fs.copySync(path.join(ROOT, 'CordovaLib', 'Classes'), path.join(projectPath, 'CordovaLib/Classes'));
        fs.copySync(path.join(ROOT, 'CordovaLib', 'VERSION'), path.join(projectPath, 'CordovaLib/VERSION'));
        fs.copySync(path.join(ROOT, 'CordovaLib', 'cordova.js'), path.join(projectPath, 'CordovaLib/cordova.js'));
        fs.copySync(path.join(ROOT, 'CordovaLib', 'CordovaLib_Prefix.pch'), path.join(projectPath, 'CordovaLib/CordovaLib_Prefix.pch'));
        fs.copySync(path.join(ROOT, 'CordovaLib', 'CordovaLib.xcodeproj', 'project.pbxproj'), path.join(projectPath, 'CordovaLib', 'CordovaLib.xcodeproj', 'project.pbxproj'));
        update_cordova_subproject([path.join(`${r}.xcodeproj`, 'project.pbxproj'), path.join(projectPath, 'CordovaLib', 'CordovaLib.xcodeproj', 'project.pbxproj'), config]);
    }
}

function copyScripts (projectPath, projectName) {
    const srcScriptsDir = path.join(ROOT, 'bin', 'templates', 'scripts', 'cordova');
    const destScriptsDir = path.join(projectPath, 'cordova');

    // Delete old scripts directory.
    fs.removeSync(destScriptsDir);

    // Copy in the new ones.
    const binDir = path.join(ROOT, 'bin');
    fs.copySync(srcScriptsDir, destScriptsDir);

    const nodeModulesDir = path.join(ROOT, 'node_modules');
    if (fs.existsSync(nodeModulesDir)) fs.copySync(nodeModulesDir, path.join(destScriptsDir, 'node_modules'));

    // Copy the check_reqs script
    fs.copySync(path.join(binDir, 'check_reqs'), path.join(destScriptsDir, 'check_reqs'));
    fs.copySync(path.join(binDir, 'check_reqs.bat'), path.join(destScriptsDir, 'check_reqs.bat'));
}