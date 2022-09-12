using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Практика_задание2.Controllers
{
    public class HomeController : Controller
    {
        private News_PortalEntities db = new News_PortalEntities();
        public ActionResult Index()
        {
            return View(db.News_draft.ToList());
        }

        [Authorize]
        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}