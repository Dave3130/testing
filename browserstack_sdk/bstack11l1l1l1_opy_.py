# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1ll1l11l_opy_ import bstack1ll11lll_opy_, bstack1l1llll1_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack1l11lll1_opy_
from bstack_utils.helper import bstack1lll1lll_opy_, bstack1l1lll11_opy_, Result
from bstack_utils.bstack1l1l1l1l_opy_ import bstack11lllll1_opy_
from bstack_utils.capture import bstack1l1l111l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l1l1l1_opy_:
    def __init__(self):
        self.bstack1l11l111_opy_ = bstack1l1l111l_opy_(self.bstack1l1l11l1_opy_)
        self.tests = {}
    @staticmethod
    def bstack1l1l11l1_opy_(log):
        if not (log[bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ॻ")] and log[bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧॼ")].strip()):
            return
        active = bstack1l11lll1_opy_.bstack11lll11l_opy_()
        log = {
            bstack11111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ॽ"): log[bstack11111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧॾ")],
            bstack11111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬॿ"): bstack1l1lll11_opy_(),
            bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫঀ"): log[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬঁ")],
        }
        if active:
            if active[bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪং")] == bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫঃ"):
                log[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ঄")] = active[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨঅ")]
            elif active[bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧআ")] == bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࠨই"):
                log[bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫঈ")] = active[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬউ")]
        bstack11lllll1_opy_.bstack1l11l1ll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l11l111_opy_.start()
        driver = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬঊ"), None)
        bstack1ll1l11l_opy_ = bstack1l1llll1_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l1lll11_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11111_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣঋ"),
            framework=bstack11111_opy_ (u"ࠨࡄࡨ࡬ࡦࡼࡥࠨঌ"),
            scope=[attrs.feature.name],
            bstack1ll11111_opy_=bstack11lllll1_opy_.bstack1lll1ll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ঍")] = bstack1ll1l11l_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ঎"), bstack1ll1l11l_opy_)
    def end_test(self, attrs):
        bstack11l11lll_opy_ = {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤএ"): attrs.feature.name,
            bstack11111_opy_ (u"ࠧࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥঐ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1ll1l11l_opy_ = self.tests[current_test_uuid][bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ঑")]
        meta = {
            bstack11111_opy_ (u"ࠢࡧࡧࡤࡸࡺࡸࡥࠣ঒"): bstack11l11lll_opy_,
            bstack11111_opy_ (u"ࠣࡵࡷࡩࡵࡹࠢও"): bstack1ll1l11l_opy_.meta.get(bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨঔ"), []),
            bstack11111_opy_ (u"ࠥࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧক"): {
                bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤখ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1ll1l11l_opy_.bstack111llll1_opy_(meta)
        bstack1ll1l11l_opy_.bstack11l111l1_opy_(bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪগ"), []))
        bstack11l11l11_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l11l11_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঘ")].stop(time=bstack1l1lll11_opy_(), duration=int(attrs.duration)*1000, result=bstack1lll111l_opy_)
        bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩঙ"), self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫচ")])
    def bstack11l1l11l_opy_(self, attrs):
        bstack1ll1ll1l_opy_ = {
            bstack11111_opy_ (u"ࠩ࡬ࡨࠬছ"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫজ"): attrs.keyword,
            bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡡࡤࡶ࡬ࡻ࡭ࡦࡰࡷࠫঝ"): [],
            bstack11111_opy_ (u"ࠬࡺࡥࡹࡶࠪঞ"): attrs.name,
            bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪট"): bstack1l1lll11_opy_(),
            bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧঠ"): bstack11111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩড"),
            bstack11111_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧঢ"): bstack11111_opy_ (u"ࠪࠫণ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧত")].add_step(bstack1ll1ll1l_opy_)
        threading.current_thread().current_step_uuid = bstack1ll1ll1l_opy_[bstack11111_opy_ (u"ࠬ࡯ࡤࠨথ")]
    def bstack11l11l1l_opy_(self, attrs):
        current_test_id = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪদ"), None)
        current_step_uuid = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡷࡩࡵࡥࡵࡶ࡫ࡧࠫধ"), None)
        bstack11l11l11_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l11l11_opy_])
        self.tests[current_test_id][bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫন")].bstack1llll1ll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1lll111l_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack111lllll_opy_(self, name, attrs):
        try:
            bstack11l11ll1_opy_ = uuid4().__str__()
            self.tests[bstack11l11ll1_opy_] = {}
            self.bstack1l11l111_opy_.start()
            scopes = []
            driver = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ঩"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࠨপ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11ll1_opy_)
            if name in [bstack11111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣফ"), bstack11111_opy_ (u"ࠧࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠣব")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢভ"), bstack11111_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠢম")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11111_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩয")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1ll11lll_opy_(
                name=name,
                uuid=bstack11l11ll1_opy_,
                started_at=bstack1l1lll11_opy_(),
                file_path=file_path,
                framework=bstack11111_opy_ (u"ࠤࡅࡩ࡭ࡧࡶࡦࠤর"),
                bstack1ll11111_opy_=bstack11lllll1_opy_.bstack1lll1ll1_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11111_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦ঱"),
                hook_type=name
            )
            self.tests[bstack11l11ll1_opy_][bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠢল")] = hook_data
            current_test_id = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠤ঳"), None)
            if current_test_id:
                hook_data.bstack11l1l111_opy_(current_test_id)
            if name == bstack11111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ঴"):
                threading.current_thread().before_all_hook_uuid = bstack11l11ll1_opy_
            threading.current_thread().current_hook_uuid = bstack11l11ll1_opy_
            bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"ࠢࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠣ঵"), hook_data)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷࡸࡥࡥࠢ࡬ࡲࠥࡹࡴࡢࡴࡷࠤ࡭ࡵ࡯࡬ࠢࡨࡺࡪࡴࡴࡴ࠮ࠣ࡬ࡴࡵ࡫ࠡࡰࡤࡱࡪࡀࠠࠦࡵ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࠪࡹࠢশ"), name, e)
    def bstack11l1l1ll_opy_(self, attrs):
        bstack1ll11ll1_opy_ = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ষ"), None)
        hook_data = self.tests[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭স")]
        status = bstack11111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦহ")
        exception = None
        bstack11l11l11_opy_ = None
        if hook_data.name == bstack11111_opy_ (u"ࠧࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠣ঺"):
            self.bstack1l11l111_opy_.reset()
            bstack11l111ll_opy_ = self.tests[bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭঻"), None)][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣ়ࠪ")].result.result
            if bstack11l111ll_opy_ == bstack11111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣঽ"):
                if attrs.hook_failures == 1:
                    status = bstack11111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤা")
                elif attrs.hook_failures == 2:
                    status = bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥি")
            elif attrs.aborted:
                status = bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦী")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩু") and attrs.hook_failures == 1:
                status = bstack11111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨূ")
            elif hasattr(attrs, bstack11111_opy_ (u"ࠧࡦࡴࡵࡳࡷࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠧৃ")) and attrs.error_message:
                status = bstack11111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣৄ")
            bstack11l11l11_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll111l_opy_ = Result(result=status, exception=exception, bstack1l11l11l_opy_=[bstack11l11l11_opy_])
        hook_data.stop(time=bstack1l1lll11_opy_(), duration=0, result=bstack1lll111l_opy_)
        bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ৅"), self.tests[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭৆")])
        threading.current_thread().current_hook_uuid = None
    def _11l1111l_opy_(self, attrs):
        try:
            import traceback
            bstack11l11111_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l11l11_opy_ = bstack11l11111_opy_[-1] if bstack11l11111_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡴࡶࡲࡱࠥࡺࡲࡢࡥࡨࡦࡦࡩ࡫ࠣে"))
            bstack11l11l11_opy_ = None
            exception = None
        return bstack11l11l11_opy_, exception