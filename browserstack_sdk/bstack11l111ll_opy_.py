# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1l11lll1_opy_ import bstack1ll1111l_opy_, bstack1lll1l1l_opy_
from bstack_utils.bstack1l1l1l1l_opy_ import bstack1l111ll1_opy_
from bstack_utils.helper import bstack11lll111_opy_, bstack1l1ll11l_opy_, Result
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1l11llll_opy_
from bstack_utils.capture import bstack1ll1llll_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l111ll_opy_:
    def __init__(self):
        self.bstack1l11111l_opy_ = bstack1ll1llll_opy_(self.bstack11llllll_opy_)
        self.tests = {}
    @staticmethod
    def bstack11llllll_opy_(log):
        if not (log[bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩॢ")] and log[bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪॣ")].strip()):
            return
        active = bstack1l111ll1_opy_.bstack1l1llll1_opy_()
        log = {
            bstack1l1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ।"): log[bstack1l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ॥")],
            bstack1l1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ०"): bstack1l1ll11l_opy_(),
            bstack1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ१"): log[bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ२")],
        }
        if active:
            if active[bstack1l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭३")] == bstack1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ४"):
                log[bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ५")] = active[bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ६")]
            elif active[bstack1l1_opy_ (u"ࠬࡺࡹࡱࡧࠪ७")] == bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࠫ८"):
                log[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ९")] = active[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ॰")]
        bstack1l11llll_opy_.bstack1l1lll1l_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l11111l_opy_.start()
        driver = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨॱ"), None)
        bstack1l11lll1_opy_ = bstack1lll1l1l_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l1ll11l_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1l1_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦॲ"),
            framework=bstack1l1_opy_ (u"ࠫࡇ࡫ࡨࡢࡸࡨࠫॳ"),
            scope=[attrs.feature.name],
            bstack1lll11l1_opy_=bstack1l11llll_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨॴ")] = bstack1l11lll1_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l11llll_opy_.bstack1ll1l11l_opy_(bstack1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧॵ"), bstack1l11lll1_opy_)
    def end_test(self, attrs):
        bstack11l1l1l1_opy_ = {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧॶ"): attrs.feature.name,
            bstack1l1_opy_ (u"ࠣࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨॷ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1l11lll1_opy_ = self.tests[current_test_uuid][bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॸ")]
        meta = {
            bstack1l1_opy_ (u"ࠥࡪࡪࡧࡴࡶࡴࡨࠦॹ"): bstack11l1l1l1_opy_,
            bstack1l1_opy_ (u"ࠦࡸࡺࡥࡱࡵࠥॺ"): bstack1l11lll1_opy_.meta.get(bstack1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫॻ"), []),
            bstack1l1_opy_ (u"ࠨࡳࡤࡧࡱࡥࡷ࡯࡯ࠣॼ"): {
                bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧॽ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1l11lll1_opy_.bstack11l1l11l_opy_(meta)
        bstack1l11lll1_opy_.bstack11l11ll1_opy_(bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ॾ"), []))
        bstack11l1ll1l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1llll111_opy_=[bstack11l1ll1l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॿ")].stop(time=bstack1l1ll11l_opy_(), duration=int(attrs.duration)*1000, result=bstack1lll1l11_opy_)
        bstack1l11llll_opy_.bstack1ll1l11l_opy_(bstack1l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬঀ"), self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧঁ")])
    def bstack11l11l11_opy_(self, attrs):
        bstack1lll1ll1_opy_ = {
            bstack1l1_opy_ (u"ࠬ࡯ࡤࠨং"): uuid4().__str__(),
            bstack1l1_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧঃ"): attrs.keyword,
            bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡤࡧࡲࡨࡷࡰࡩࡳࡺࠧ঄"): [],
            bstack1l1_opy_ (u"ࠨࡶࡨࡼࡹ࠭অ"): attrs.name,
            bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭আ"): bstack1l1ll11l_opy_(),
            bstack1l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪই"): bstack1l1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬঈ"),
            bstack1l1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪউ"): bstack1l1_opy_ (u"࠭ࠧঊ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪঋ")].add_step(bstack1lll1ll1_opy_)
        threading.current_thread().current_step_uuid = bstack1lll1ll1_opy_[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫঌ")]
    def bstack11l1ll11_opy_(self, attrs):
        current_test_id = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭঍"), None)
        current_step_uuid = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧ঎"), None)
        bstack11l1ll1l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1llll111_opy_=[bstack11l1ll1l_opy_])
        self.tests[current_test_id][bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧএ")].bstack1lll1lll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1lll1l11_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l11lll_opy_(self, name, attrs):
        try:
            bstack11l11l1l_opy_ = uuid4().__str__()
            self.tests[bstack11l11l1l_opy_] = {}
            self.bstack1l11111l_opy_.start()
            scopes = []
            driver = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫঐ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫ঑")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11l1l_opy_)
            if name in [bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ঒"), bstack1l1_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦও")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥঔ"), bstack1l1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠥক")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1l1_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬখ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1ll1111l_opy_(
                name=name,
                uuid=bstack11l11l1l_opy_,
                started_at=bstack1l1ll11l_opy_(),
                file_path=file_path,
                framework=bstack1l1_opy_ (u"ࠧࡈࡥࡩࡣࡹࡩࠧগ"),
                bstack1lll11l1_opy_=bstack1l11llll_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1l1_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢঘ"),
                hook_type=name
            )
            self.tests[bstack11l11l1l_opy_][bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡡࡵࡣࠥঙ")] = hook_data
            current_test_id = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠣࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠧচ"), None)
            if current_test_id:
                hook_data.bstack11l1l1ll_opy_(current_test_id)
            if name == bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨছ"):
                threading.current_thread().before_all_hook_uuid = bstack11l11l1l_opy_
            threading.current_thread().current_hook_uuid = bstack11l11l1l_opy_
            bstack1l11llll_opy_.bstack1ll1l11l_opy_(bstack1l1_opy_ (u"ࠥࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠦজ"), hook_data)
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࠠࡩࡱࡲ࡯ࠥ࡫ࡶࡦࡰࡷࡷ࠱ࠦࡨࡰࡱ࡮ࠤࡳࡧ࡭ࡦ࠼ࠣࠩࡸ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠦࡵࠥঝ"), name, e)
    def bstack11l1lll1_opy_(self, attrs):
        bstack1lll1111_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩঞ"), None)
        hook_data = self.tests[bstack1lll1111_opy_][bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩট")]
        status = bstack1l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢঠ")
        exception = None
        bstack11l1ll1l_opy_ = None
        if hook_data.name == bstack1l1_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦড"):
            self.bstack1l11111l_opy_.reset()
            bstack11l1llll_opy_ = self.tests[bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩঢ"), None)][bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ণ")].result.result
            if bstack11l1llll_opy_ == bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦত"):
                if attrs.hook_failures == 1:
                    status = bstack1l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧথ")
                elif attrs.hook_failures == 2:
                    status = bstack1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨদ")
            elif attrs.aborted:
                status = bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢধ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬন") and attrs.hook_failures == 1:
                status = bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ঩")
            elif hasattr(attrs, bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪপ")) and attrs.error_message:
                status = bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦফ")
            bstack11l1ll1l_opy_, exception = self._11l111l1_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=status, exception=exception, bstack1llll111_opy_=[bstack11l1ll1l_opy_])
        hook_data.stop(time=bstack1l1ll11l_opy_(), duration=0, result=bstack1lll1l11_opy_)
        bstack1l11llll_opy_.bstack1ll1l11l_opy_(bstack1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧব"), self.tests[bstack1lll1111_opy_][bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩভ")])
        threading.current_thread().current_hook_uuid = None
    def _11l111l1_opy_(self, attrs):
        try:
            import traceback
            bstack11l1l111_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1ll1l_opy_ = bstack11l1l111_opy_[-1] if bstack11l1l111_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࠦম"))
            bstack11l1ll1l_opy_ = None
            exception = None
        return bstack11l1ll1l_opy_, exception