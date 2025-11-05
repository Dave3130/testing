# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1lll1l11_opy_ import bstack1llll111_opy_, bstack1l1ll1ll_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1l11l1l1_opy_
from bstack_utils.helper import bstack1l1l1ll1_opy_, bstack1ll111ll_opy_, Result
from bstack_utils.bstack1llll1ll_opy_ import bstack1ll1l111_opy_
from bstack_utils.capture import bstack1ll1l1ll_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l1l11l_opy_:
    def __init__(self):
        self.bstack1l111l11_opy_ = bstack1ll1l1ll_opy_(self.bstack1lll11ll_opy_)
        self.tests = {}
    @staticmethod
    def bstack1lll11ll_opy_(log):
        if not (log[bstack11ll1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧॼ")] and log[bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨॽ")].strip()):
            return
        active = bstack1l11l1l1_opy_.bstack1l11111l_opy_()
        log = {
            bstack11ll1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧॾ"): log[bstack11ll1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨॿ")],
            bstack11ll1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ঀ"): bstack1ll111ll_opy_(),
            bstack11ll1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬঁ"): log[bstack11ll1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ং")],
        }
        if active:
            if active[bstack11ll1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫঃ")] == bstack11ll1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ঄"):
                log[bstack11ll1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨঅ")] = active[bstack11ll1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩআ")]
            elif active[bstack11ll1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨই")] == bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩঈ"):
                log[bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬউ")] = active[bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ঊ")]
        bstack1ll1l111_opy_.bstack1l1111ll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l111l11_opy_.start()
        driver = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ঋ"), None)
        bstack1lll1l11_opy_ = bstack1l1ll1ll_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1ll111ll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11ll1ll_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤঌ"),
            framework=bstack11ll1ll_opy_ (u"ࠩࡅࡩ࡭ࡧࡶࡦࠩ঍"),
            scope=[attrs.feature.name],
            bstack1l1l11ll_opy_=bstack1ll1l111_opy_.bstack1ll1ll1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭঎")] = bstack1lll1l11_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1ll1l111_opy_.bstack1l1lll1l_opy_(bstack11ll1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬএ"), bstack1lll1l11_opy_)
    def end_test(self, attrs):
        bstack11l11111_opy_ = {
            bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥঐ"): attrs.feature.name,
            bstack11ll1ll_opy_ (u"ࠨࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦ঑"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1lll1l11_opy_ = self.tests[current_test_uuid][bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ঒")]
        meta = {
            bstack11ll1ll_opy_ (u"ࠣࡨࡨࡥࡹࡻࡲࡦࠤও"): bstack11l11111_opy_,
            bstack11ll1ll_opy_ (u"ࠤࡶࡸࡪࡶࡳࠣঔ"): bstack1lll1l11_opy_.meta.get(bstack11ll1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩক"), []),
            bstack11ll1ll_opy_ (u"ࠦࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨখ"): {
                bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥগ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1lll1l11_opy_.bstack111lllll_opy_(meta)
        bstack1lll1l11_opy_.bstack11l111ll_opy_(bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫঘ"), []))
        bstack11l11lll_opy_, exception = self._111llll1_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l11lll_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪঙ")].stop(time=bstack1ll111ll_opy_(), duration=int(attrs.duration)*1000, result=bstack1lll111l_opy_)
        bstack1ll1l111_opy_.bstack1l1lll1l_opy_(bstack11ll1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪচ"), self.tests[threading.current_thread().current_test_uuid][bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬছ")])
    def bstack11l1l1ll_opy_(self, attrs):
        bstack1l111l1l_opy_ = {
            bstack11ll1ll_opy_ (u"ࠪ࡭ࡩ࠭জ"): uuid4().__str__(),
            bstack11ll1ll_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬঝ"): attrs.keyword,
            bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡢࡥࡷ࡭ࡵ࡮ࡧࡱࡸࠬঞ"): [],
            bstack11ll1ll_opy_ (u"࠭ࡴࡦࡺࡷࠫট"): attrs.name,
            bstack11ll1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫঠ"): bstack1ll111ll_opy_(),
            bstack11ll1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨড"): bstack11ll1ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪঢ"),
            bstack11ll1ll_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨণ"): bstack11ll1ll_opy_ (u"ࠫࠬত")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨথ")].add_step(bstack1l111l1l_opy_)
        threading.current_thread().current_step_uuid = bstack1l111l1l_opy_[bstack11ll1ll_opy_ (u"࠭ࡩࡥࠩদ")]
    def bstack11l1l111_opy_(self, attrs):
        current_test_id = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫধ"), None)
        current_step_uuid = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡸࡪࡶ࡟ࡶࡷ࡬ࡨࠬন"), None)
        bstack11l11lll_opy_, exception = self._111llll1_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l11lll_opy_])
        self.tests[current_test_id][bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ঩")].bstack1ll111l1_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1lll111l_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l11ll1_opy_(self, name, attrs):
        try:
            bstack11l111l1_opy_ = uuid4().__str__()
            self.tests[bstack11l111l1_opy_] = {}
            self.bstack1l111l11_opy_.start()
            scopes = []
            driver = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩপ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11ll1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩফ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l111l1_opy_)
            if name in [bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤব"), bstack11ll1ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤভ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11ll1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣম"), bstack11ll1ll_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠣয")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11ll1ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪর")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1llll111_opy_(
                name=name,
                uuid=bstack11l111l1_opy_,
                started_at=bstack1ll111ll_opy_(),
                file_path=file_path,
                framework=bstack11ll1ll_opy_ (u"ࠥࡆࡪ࡮ࡡࡷࡧࠥ঱"),
                bstack1l1l11ll_opy_=bstack1ll1l111_opy_.bstack1ll1ll1l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11ll1ll_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧল"),
                hook_type=name
            )
            self.tests[bstack11l111l1_opy_][bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡦࡺࡡࠣ঳")] = hook_data
            current_test_id = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠥ঴"), None)
            if current_test_id:
                hook_data.bstack11l1l1l1_opy_(current_test_id)
            if name == bstack11ll1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ঵"):
                threading.current_thread().before_all_hook_uuid = bstack11l111l1_opy_
            threading.current_thread().current_hook_uuid = bstack11l111l1_opy_
            bstack1ll1l111_opy_.bstack1l1lll1l_opy_(bstack11ll1ll_opy_ (u"ࠣࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠤশ"), hook_data)
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣ࡭ࡳࠦࡳࡵࡣࡵࡸࠥ࡮࡯ࡰ࡭ࠣࡩࡻ࡫࡮ࡵࡵ࠯ࠤ࡭ࡵ࡯࡬ࠢࡱࡥࡲ࡫࠺ࠡࠧࡶ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠫࡳࠣষ"), name, e)
    def bstack11l11l11_opy_(self, attrs):
        bstack1ll1111l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧস"), None)
        hook_data = self.tests[bstack1ll1111l_opy_][bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧহ")]
        status = bstack11ll1ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ঺")
        exception = None
        bstack11l11lll_opy_ = None
        if hook_data.name == bstack11ll1ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤ঻"):
            self.bstack1l111l11_opy_.reset()
            bstack11l11l1l_opy_ = self.tests[bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪ়ࠧ"), None)][bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫঽ")].result.result
            if bstack11l11l1l_opy_ == bstack11ll1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤা"):
                if attrs.hook_failures == 1:
                    status = bstack11ll1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥি")
                elif attrs.hook_failures == 2:
                    status = bstack11ll1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦী")
            elif attrs.aborted:
                status = bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧু")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11ll1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪূ") and attrs.hook_failures == 1:
                status = bstack11ll1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢৃ")
            elif hasattr(attrs, bstack11ll1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨৄ")) and attrs.error_message:
                status = bstack11ll1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ৅")
            bstack11l11lll_opy_, exception = self._111llll1_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=status, exception=exception, bstack1l11l11l_opy_=[bstack11l11lll_opy_])
        hook_data.stop(time=bstack1ll111ll_opy_(), duration=0, result=bstack1lll111l_opy_)
        bstack1ll1l111_opy_.bstack1l1lll1l_opy_(bstack11ll1ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ৆"), self.tests[bstack1ll1111l_opy_][bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧে")])
        threading.current_thread().current_hook_uuid = None
    def _111llll1_opy_(self, attrs):
        try:
            import traceback
            bstack11l1111l_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l11lll_opy_ = bstack11l1111l_opy_[-1] if bstack11l1111l_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡵࡷࡳࡲࠦࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࠤৈ"))
            bstack11l11lll_opy_ = None
            exception = None
        return bstack11l11lll_opy_, exception