# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1ll1l1l1_opy_ import bstack1lll1l11_opy_, bstack1ll1lll1_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1lll1lll_opy_
from bstack_utils.helper import bstack1l1lll11_opy_, bstack11lllll1_opy_, Result
from bstack_utils.bstack1l1111ll_opy_ import bstack1lll111l_opy_
from bstack_utils.capture import bstack1lll1l1l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l11111_opy_:
    def __init__(self):
        self.bstack1l11ll1l_opy_ = bstack1lll1l1l_opy_(self.bstack1ll1ll1l_opy_)
        self.tests = {}
    @staticmethod
    def bstack1ll1ll1l_opy_(log):
        if not (log[bstack11l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ३")] and log[bstack11l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ४")].strip()):
            return
        active = bstack1lll1lll_opy_.bstack11lll1l1_opy_()
        log = {
            bstack11l111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ५"): log[bstack11l111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ६")],
            bstack11l111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ७"): bstack11lllll1_opy_(),
            bstack11l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ८"): log[bstack11l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ९")],
        }
        if active:
            if active[bstack11l111_opy_ (u"ࠨࡶࡼࡴࡪ࠭॰")] == bstack11l111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧॱ"):
                log[bstack11l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॲ")] = active[bstack11l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫॳ")]
            elif active[bstack11l111_opy_ (u"ࠬࡺࡹࡱࡧࠪॴ")] == bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࠫॵ"):
                log[bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧॶ")] = active[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨॷ")]
        bstack1lll111l_opy_.bstack1ll1l111_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l11ll1l_opy_.start()
        driver = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨॸ"), None)
        bstack1ll1l1l1_opy_ = bstack1ll1lll1_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack11lllll1_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11l111_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦॹ"),
            framework=bstack11l111_opy_ (u"ࠫࡇ࡫ࡨࡢࡸࡨࠫॺ"),
            scope=[attrs.feature.name],
            bstack1ll11l11_opy_=bstack1lll111l_opy_.bstack1ll1l11l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨॻ")] = bstack1ll1l1l1_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1lll111l_opy_.bstack1l1111l1_opy_(bstack11l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧॼ"), bstack1ll1l1l1_opy_)
    def end_test(self, attrs):
        bstack11l1l11l_opy_ = {
            bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧॽ"): attrs.feature.name,
            bstack11l111_opy_ (u"ࠣࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨॾ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1ll1l1l1_opy_ = self.tests[current_test_uuid][bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॿ")]
        meta = {
            bstack11l111_opy_ (u"ࠥࡪࡪࡧࡴࡶࡴࡨࠦঀ"): bstack11l1l11l_opy_,
            bstack11l111_opy_ (u"ࠦࡸࡺࡥࡱࡵࠥঁ"): bstack1ll1l1l1_opy_.meta.get(bstack11l111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫং"), []),
            bstack11l111_opy_ (u"ࠨࡳࡤࡧࡱࡥࡷ࡯࡯ࠣঃ"): {
                bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ঄"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1ll1l1l1_opy_.bstack11l11lll_opy_(meta)
        bstack1ll1l1l1_opy_.bstack11l11ll1_opy_(bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭অ"), []))
        bstack11l111ll_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l11ll11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l1ll11l_opy_=[bstack11l111ll_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬআ")].stop(time=bstack11lllll1_opy_(), duration=int(attrs.duration)*1000, result=bstack1l11ll11_opy_)
        bstack1lll111l_opy_.bstack1l1111l1_opy_(bstack11l111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬই"), self.tests[threading.current_thread().current_test_uuid][bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧঈ")])
    def bstack11l1l1l1_opy_(self, attrs):
        bstack1llll11l_opy_ = {
            bstack11l111_opy_ (u"ࠬ࡯ࡤࠨউ"): uuid4().__str__(),
            bstack11l111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧঊ"): attrs.keyword,
            bstack11l111_opy_ (u"ࠧࡴࡶࡨࡴࡤࡧࡲࡨࡷࡰࡩࡳࡺࠧঋ"): [],
            bstack11l111_opy_ (u"ࠨࡶࡨࡼࡹ࠭ঌ"): attrs.name,
            bstack11l111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭঍"): bstack11lllll1_opy_(),
            bstack11l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ঎"): bstack11l111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬএ"),
            bstack11l111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪঐ"): bstack11l111_opy_ (u"࠭ࠧ঑")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ঒")].add_step(bstack1llll11l_opy_)
        threading.current_thread().current_step_uuid = bstack1llll11l_opy_[bstack11l111_opy_ (u"ࠨ࡫ࡧࠫও")]
    def bstack11l11l11_opy_(self, attrs):
        current_test_id = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ঔ"), None)
        current_step_uuid = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧক"), None)
        bstack11l111ll_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l11ll11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l1ll11l_opy_=[bstack11l111ll_opy_])
        self.tests[current_test_id][bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧখ")].bstack1l1l11l1_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1l11ll11_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l111l1_opy_(self, name, attrs):
        try:
            bstack11l11l1l_opy_ = uuid4().__str__()
            self.tests[bstack11l11l1l_opy_] = {}
            self.bstack1l11ll1l_opy_.start()
            scopes = []
            driver = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫগ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫঘ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11l1l_opy_)
            if name in [bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦঙ"), bstack11l111_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦচ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥছ"), bstack11l111_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠥজ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11l111_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬঝ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1lll1l11_opy_(
                name=name,
                uuid=bstack11l11l1l_opy_,
                started_at=bstack11lllll1_opy_(),
                file_path=file_path,
                framework=bstack11l111_opy_ (u"ࠧࡈࡥࡩࡣࡹࡩࠧঞ"),
                bstack1ll11l11_opy_=bstack1lll111l_opy_.bstack1ll1l11l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11l111_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢট"),
                hook_type=name
            )
            self.tests[bstack11l11l1l_opy_][bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡡࡵࡣࠥঠ")] = hook_data
            current_test_id = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠣࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠧড"), None)
            if current_test_id:
                hook_data.bstack111lll1l_opy_(current_test_id)
            if name == bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨঢ"):
                threading.current_thread().before_all_hook_uuid = bstack11l11l1l_opy_
            threading.current_thread().current_hook_uuid = bstack11l11l1l_opy_
            bstack1lll111l_opy_.bstack1l1111l1_opy_(bstack11l111_opy_ (u"ࠥࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠦণ"), hook_data)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࠠࡩࡱࡲ࡯ࠥ࡫ࡶࡦࡰࡷࡷ࠱ࠦࡨࡰࡱ࡮ࠤࡳࡧ࡭ࡦ࠼ࠣࠩࡸ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠦࡵࠥত"), name, e)
    def bstack111llll1_opy_(self, attrs):
        bstack1ll111ll_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩথ"), None)
        hook_data = self.tests[bstack1ll111ll_opy_][bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩদ")]
        status = bstack11l111_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢধ")
        exception = None
        bstack11l111ll_opy_ = None
        if hook_data.name == bstack11l111_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦন"):
            self.bstack1l11ll1l_opy_.reset()
            bstack111lllll_opy_ = self.tests[bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ঩"), None)][bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭প")].result.result
            if bstack111lllll_opy_ == bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦফ"):
                if attrs.hook_failures == 1:
                    status = bstack11l111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧব")
                elif attrs.hook_failures == 2:
                    status = bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨভ")
            elif attrs.aborted:
                status = bstack11l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢম")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11l111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬয") and attrs.hook_failures == 1:
                status = bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤর")
            elif hasattr(attrs, bstack11l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪ঱")) and attrs.error_message:
                status = bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦল")
            bstack11l111ll_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l11ll11_opy_ = Result(result=status, exception=exception, bstack1l1ll11l_opy_=[bstack11l111ll_opy_])
        hook_data.stop(time=bstack11lllll1_opy_(), duration=0, result=bstack1l11ll11_opy_)
        bstack1lll111l_opy_.bstack1l1111l1_opy_(bstack11l111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ঳"), self.tests[bstack1ll111ll_opy_][bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ঴")])
        threading.current_thread().current_hook_uuid = None
    def _11l1l111_opy_(self, attrs):
        try:
            import traceback
            bstack11l1111l_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l111ll_opy_ = bstack11l1111l_opy_[-1] if bstack11l1111l_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࠦ঵"))
            bstack11l111ll_opy_ = None
            exception = None
        return bstack11l111ll_opy_, exception