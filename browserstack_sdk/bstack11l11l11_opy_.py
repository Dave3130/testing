# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1l11ll1l_opy_ import bstack1l111ll1_opy_, bstack1l1l1l11_opy_
from bstack_utils.bstack1l1ll1l1_opy_ import bstack1l1l111l_opy_
from bstack_utils.helper import bstack1l1l11l1_opy_, bstack1lll1111_opy_, Result
from bstack_utils.bstack11lll1l1_opy_ import bstack1l111l1l_opy_
from bstack_utils.capture import bstack1ll1ll1l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l11l11_opy_:
    def __init__(self):
        self.bstack11lll1ll_opy_ = bstack1ll1ll1l_opy_(self.bstack1ll1llll_opy_)
        self.tests = {}
    @staticmethod
    def bstack1ll1llll_opy_(log):
        if not (log[bstack11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ५")] and log[bstack11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ६")].strip()):
            return
        active = bstack1l1l111l_opy_.bstack1ll11l11_opy_()
        log = {
            bstack11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ७"): log[bstack11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ८")],
            bstack11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ९"): bstack1lll1111_opy_(),
            bstack11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ॰"): log[bstack11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪॱ")],
        }
        if active:
            if active[bstack11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨॲ")] == bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩॳ"):
                log[bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬॴ")] = active[bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ॵ")]
            elif active[bstack11ll_opy_ (u"ࠧࡵࡻࡳࡩࠬॶ")] == bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹ࠭ॷ"):
                log[bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩॸ")] = active[bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॹ")]
        bstack1l111l1l_opy_.bstack1l11l1ll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack11lll1ll_opy_.start()
        driver = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪॺ"), None)
        bstack1l11ll1l_opy_ = bstack1l1l1l11_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1lll1111_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11ll_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨॻ"),
            framework=bstack11ll_opy_ (u"࠭ࡂࡦࡪࡤࡺࡪ࠭ॼ"),
            scope=[attrs.feature.name],
            bstack1l1ll111_opy_=bstack1l111l1l_opy_.bstack1l1lll1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪॽ")] = bstack1l11ll1l_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩॾ"), bstack1l11ll1l_opy_)
    def end_test(self, attrs):
        bstack11l11111_opy_ = {
            bstack11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢॿ"): attrs.feature.name,
            bstack11ll_opy_ (u"ࠥࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣঀ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1l11ll1l_opy_ = self.tests[current_test_uuid][bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧঁ")]
        meta = {
            bstack11ll_opy_ (u"ࠧ࡬ࡥࡢࡶࡸࡶࡪࠨং"): bstack11l11111_opy_,
            bstack11ll_opy_ (u"ࠨࡳࡵࡧࡳࡷࠧঃ"): bstack1l11ll1l_opy_.meta.get(bstack11ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭঄"), []),
            bstack11ll_opy_ (u"ࠣࡵࡦࡩࡳࡧࡲࡪࡱࠥঅ"): {
                bstack11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢআ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1l11ll1l_opy_.bstack11l1111l_opy_(meta)
        bstack1l11ll1l_opy_.bstack111lll1l_opy_(bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࠨই"), []))
        bstack11l1l11l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1ll1l1l1_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l1l11l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧঈ")].stop(time=bstack1lll1111_opy_(), duration=int(attrs.duration)*1000, result=bstack1ll1l1l1_opy_)
        bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧউ"), self.tests[threading.current_thread().current_test_uuid][bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঊ")])
    def bstack11l11lll_opy_(self, attrs):
        bstack1ll111l1_opy_ = {
            bstack11ll_opy_ (u"ࠧࡪࡦࠪঋ"): uuid4().__str__(),
            bstack11ll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩঌ"): attrs.keyword,
            bstack11ll_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩ঍"): [],
            bstack11ll_opy_ (u"ࠪࡸࡪࡾࡴࠨ঎"): attrs.name,
            bstack11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨএ"): bstack1lll1111_opy_(),
            bstack11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬঐ"): bstack11ll_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ঑"),
            bstack11ll_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ঒"): bstack11ll_opy_ (u"ࠨࠩও")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬঔ")].add_step(bstack1ll111l1_opy_)
        threading.current_thread().current_step_uuid = bstack1ll111l1_opy_[bstack11ll_opy_ (u"ࠪ࡭ࡩ࠭ক")]
    def bstack11l11ll1_opy_(self, attrs):
        current_test_id = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨখ"), None)
        current_step_uuid = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡵࡧࡳࡣࡺࡻࡩࡥࠩগ"), None)
        bstack11l1l11l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1ll1l1l1_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11l11l_opy_=[bstack11l1l11l_opy_])
        self.tests[current_test_id][bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঘ")].bstack1l111lll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1ll1l1l1_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l111ll_opy_(self, name, attrs):
        try:
            bstack11l11l1l_opy_ = uuid4().__str__()
            self.tests[bstack11l11l1l_opy_] = {}
            self.bstack11lll1ll_opy_.start()
            scopes = []
            driver = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ঙ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭চ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11l1l_opy_)
            if name in [bstack11ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨছ"), bstack11ll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡤࡰࡱࠨজ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧঝ"), bstack11ll_opy_ (u"ࠧࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠧঞ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11ll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧট")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l111ll1_opy_(
                name=name,
                uuid=bstack11l11l1l_opy_,
                started_at=bstack1lll1111_opy_(),
                file_path=file_path,
                framework=bstack11ll_opy_ (u"ࠢࡃࡧ࡫ࡥࡻ࡫ࠢঠ"),
                bstack1l1ll111_opy_=bstack1l111l1l_opy_.bstack1l1lll1l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11ll_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤড"),
                hook_type=name
            )
            self.tests[bstack11l11l1l_opy_][bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠧঢ")] = hook_data
            current_test_id = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠥࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠢণ"), None)
            if current_test_id:
                hook_data.bstack111lllll_opy_(current_test_id)
            if name == bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣত"):
                threading.current_thread().before_all_hook_uuid = bstack11l11l1l_opy_
            threading.current_thread().current_hook_uuid = bstack11l11l1l_opy_
            bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩࠨথ"), hook_data)
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡪࡰࠣࡷࡹࡧࡲࡵࠢ࡫ࡳࡴࡱࠠࡦࡸࡨࡲࡹࡹࠬࠡࡪࡲࡳࡰࠦ࡮ࡢ࡯ࡨ࠾ࠥࠫࡳ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠨࡷࠧদ"), name, e)
    def bstack11l1l111_opy_(self, attrs):
        bstack1l11l1l1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫধ"), None)
        hook_data = self.tests[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫন")]
        status = bstack11ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ঩")
        exception = None
        bstack11l1l11l_opy_ = None
        if hook_data.name == bstack11ll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡤࡰࡱࠨপ"):
            self.bstack11lll1ll_opy_.reset()
            bstack111lll11_opy_ = self.tests[bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫফ"), None)][bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨব")].result.result
            if bstack111lll11_opy_ == bstack11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨভ"):
                if attrs.hook_failures == 1:
                    status = bstack11ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢম")
                elif attrs.hook_failures == 2:
                    status = bstack11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣয")
            elif attrs.aborted:
                status = bstack11ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤর")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧ঱") and attrs.hook_failures == 1:
                status = bstack11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦল")
            elif hasattr(attrs, bstack11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬ঳")) and attrs.error_message:
                status = bstack11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ঴")
            bstack11l1l11l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1ll1l1l1_opy_ = Result(result=status, exception=exception, bstack1l11l11l_opy_=[bstack11l1l11l_opy_])
        hook_data.stop(time=bstack1lll1111_opy_(), duration=0, result=bstack1ll1l1l1_opy_)
        bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ঵"), self.tests[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫশ")])
        threading.current_thread().current_hook_uuid = None
    def _11l111l1_opy_(self, attrs):
        try:
            import traceback
            bstack111llll1_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1l11l_opy_ = bstack111llll1_opy_[-1] if bstack111llll1_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡷࡧࡣࡦࡤࡤࡧࡰࠨষ"))
            bstack11l1l11l_opy_ = None
            exception = None
        return bstack11l1l11l_opy_, exception