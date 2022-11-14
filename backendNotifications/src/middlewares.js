function notFound(req, res, next) {
  res.status(404);
  next(new Error(`Error 404: ${req.originalUrl} not found.`));
}

// Error handler
function errorHandler(err, _req, res, _next) {
  res.status(err.status || 500);
  res.json({
    message: err.message,
    stack: process.env.NODE_ENV === 'production' ? '' : err.stack,
  });
}

module.exports = {
  notFound,
  errorHandler,
};
