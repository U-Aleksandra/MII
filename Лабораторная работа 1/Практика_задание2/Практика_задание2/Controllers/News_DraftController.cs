using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.Mvc;


namespace Практика_задание2.Controllers
{
    [Authorize]
    public class News_DraftController : Controller
    {
        private News_PortalEntities db = new News_PortalEntities();
        // GET: News_Draft
        public ActionResult Index()
        {
            return View(db.News_draft.ToList());
        }

        
        [HttpGet]
        [Authorize(Roles="admin")]
        public ActionResult Create_News()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Create_News(News_draft news_draft)
        {
           
            db.News_draft.Add(news_draft);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        [HttpGet]
        [Authorize(Roles = "admin")]
        public ActionResult Delete_News(int id)
        {
            News_draft nd = db.News_draft.Find(id);
            if(nd == null)
            {
                return HttpNotFound();
            }
            return View(nd);
        }

        [HttpPost, ActionName("Delete_News")]
        public ActionResult DeleteConfirmed(int id)
        {
            News_draft nd = db.News_draft.Find(id);
            if (nd == null)
            {
                return HttpNotFound();
            }
            db.News_draft.Remove(nd);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        [HttpGet]
        [Authorize(Roles = "admin")]
        public ActionResult Edit_News(int? id)
        {
            if (id == null)
            {
                return HttpNotFound();
            }
            News_draft nd = db.News_draft.Find(id);
            if (nd != null)
            {
                return View(nd);
            }
            return HttpNotFound();
        }

        [HttpPost]
        public ActionResult Edit_News(News_draft nd)
        {
          
            db.Entry(nd).State = System.Data.Entity.EntityState.Modified;
            db.SaveChanges();
            return RedirectToAction("Index");
        }

       
        [Authorize]
        public ActionResult Publish_News(int? id)
        {
            if (id == null)
            {
                return HttpNotFound();
            }
            News_draft nd = db.News_draft.Find(id);
            if (nd != null)
            {
                return View(nd);
            }
            return HttpNotFound();
        }

        [HttpPost]
        [Authorize]
        public ActionResult Publish_News(int id)
        {
            var news = db.News_draft.Where(m => m.ID == id).FirstOrDefault();
            news.publish = true;
            db.SaveChanges();
            return RedirectToAction("Index");
        }


    }
}