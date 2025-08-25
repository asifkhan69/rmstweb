let gulp = require("gulp"),
    babel = require("gulp-babel"),
    tap = require('gulp-tap'),
    buffer = require('gulp-buffer'),
    babelify = require('babelify'),
    browserify = require('browserify'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    gap = require('gulp-append-prepend'),
    sass = require('gulp-sass')(require('node-sass'));

// default standalone file
gulp.task("default", () => {
    return gulp.src("rmstweb/simple-lightbox.js",{ read: false})
        .pipe(tap(function(file) {
            // replace file contents with browserify's bundle stream
            file.contents = browserify({
                entries: file.path,
                debug: false
            })
            .transform(babelify)
            .bundle();
        }))
        .pipe(buffer())
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest("dist"));
});

// legacy for IE11
gulp.task("legacy", () => {
    return gulp.src("rmstweb/legacy.js",{ read: false })
        .pipe(tap(function(file) {
            file.contents = browserify({
                entries: file.path,
                debug: false
            })
            .transform(babelify, {presets: [
                ["@babel/preset-env", {
                        "useBuiltIns": "usage",
                        "corejs": "3.14.0"
                    }
                ]
            ]})
            .bundle();
        }))
        .pipe(buffer())
        .pipe(rename('simple-lightbox.legacy.js'))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest("dist"));
});

// use it with modules
gulp.task("modules", () => {
    return gulp.src("rmstweb/simple-lightbox.js")
        .pipe(babel())
        .pipe(rename('simple-lightbox.modules.js'))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest("dist"));
});

// pure file as ecmascript module
gulp.task("esm", () => {
    return gulp.src("rmstweb/simple-lightbox.js")
        .pipe(rename('simple-lightbox.esm.js'))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest("dist"));
});

// use it with jquery
gulp.task("jquery", () => {
    return gulp.src("rmstweb/jquery-plugin-wrap.js",{ read: false })
        .pipe(tap(function(file) {
            file.contents = browserify({
                entries: file.path,
                debug: false
            })
                .transform(babelify)
                .bundle();
        }))
        .pipe(buffer())
        .pipe(rename('simple-lightbox.jquery.js'))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest("dist"));
});

gulp.task('minify', () => {
    return gulp.src("dist/simple-lightbox.js")
        .pipe(uglify())
        .pipe(rename('simple-lightbox.min.js'))
        .pipe(gulp.dest('dist/'));
});

gulp.task('legacy-minify', () => {
    return gulp.src("dist/simple-lightbox.legacy.js")
        .pipe(uglify())
        .pipe(rename('simple-lightbox.legacy.min.js'))
        .pipe(gulp.dest('dist/'));
});

gulp.task('jquery-minify', () => {
    return gulp.src("dist/simple-lightbox.jquery.js")
        .pipe(uglify())
        .pipe(rename('simple-lightbox.jquery.min.js'))
        .pipe(gulp.dest('dist/'));
});

gulp.task('sass', () => {
    return gulp.src('./rmstweb/*.scss')
        .pipe(sass({}))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest('./dist'));
});

gulp.task('sass-minify', () => {
    return gulp.src('./rmstweb/*.scss')
        .pipe(sass({outputStyle: 'compressed'}))
        .pipe(rename('simple-lightbox.min.css'))
        .pipe(gap.prependFile('./rmstweb/license-notice.txt'))
        .pipe(gulp.dest('./dist'));
});

gulp.task('build', gulp.series('default', 'legacy', 'modules', 'esm', 'jquery', 'minify', 'legacy-minify', 'jquery-minify', 'sass', 'sass-minify'));

gulp.task('watch', () => {
    gulp.watch('./rmstweb/*.js', gulp.series('default'));
    gulp.watch('./rmstweb/*.scss', gulp.series('sass'));
});
