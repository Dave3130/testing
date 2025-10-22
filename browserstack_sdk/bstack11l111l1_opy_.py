# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack11lll1ll_opy_ import bstack1l11llll_opy_, bstack1lllll11_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.helper import bstack1l11l1l1_opy_, bstack1l1111ll_opy_, Result
from bstack_utils.bstack1l1ll111_opy_ import bstack1ll1l1l1_opy_
from bstack_utils.capture import bstack1l1l1lll_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l111l1_opy_:
    def __init__(self):
        self.bstack1l11111l_opy_ = bstack1l1l1lll_opy_(self.bstack1llll1ll_opy_)
        self.tests = {}
    @staticmethod
    def bstack1llll1ll_opy_(log):
        if not (log[bstack1lllll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ३")] and log[bstack1lllll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ४")].strip()):
            return
        active = bstack1ll11l1l_opy_.bstack1ll1ll1l_opy_()
        log = {
            bstack1lllll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ५"): log[bstack1lllll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ६")],
            bstack1lllll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ७"): bstack1l1111ll_opy_(),
            bstack1lllll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ८"): log[bstack1lllll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ९")],
        }
        if active:
            if active[bstack1lllll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭॰")] == bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧॱ"):
                log[bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॲ")] = active[bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫॳ")]
            elif active[bstack1lllll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪॴ")] == bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࠫॵ"):
                log[bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧॶ")] = active[bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨॷ")]
        bstack1ll1l1l1_opy_.bstack1ll1llll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l11111l_opy_.start()
        driver = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨॸ"), None)
        bstack11lll1ll_opy_ = bstack1lllll11_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l1111ll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1lllll1l_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦॹ"),
            framework=bstack1lllll1l_opy_ (u"ࠫࡇ࡫ࡨࡢࡸࡨࠫॺ"),
            scope=[attrs.feature.name],
            bstack11lll111_opy_=bstack1ll1l1l1_opy_.bstack1ll111l1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨॻ")] = bstack11lll1ll_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧॼ"), bstack11lll1ll_opy_)
    def end_test(self, attrs):
        bstack11l1l11l_opy_ = {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧॽ"): attrs.feature.name,
            bstack1lllll1l_opy_ (u"ࠣࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨॾ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack11lll1ll_opy_ = self.tests[current_test_uuid][bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॿ")]
        meta = {
            bstack1lllll1l_opy_ (u"ࠥࡪࡪࡧࡴࡶࡴࡨࠦঀ"): bstack11l1l11l_opy_,
            bstack1lllll1l_opy_ (u"ࠦࡸࡺࡥࡱࡵࠥঁ"): bstack11lll1ll_opy_.meta.get(bstack1lllll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫং"), []),
            bstack1lllll1l_opy_ (u"ࠨࡳࡤࡧࡱࡥࡷ࡯࡯ࠣঃ"): {
                bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ঄"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack11lll1ll_opy_.bstack11l11l11_opy_(meta)
        bstack11lll1ll_opy_.bstack11l11ll1_opy_(bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭অ"), []))
        bstack11l111ll_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1lll11l1_opy_=[bstack11l111ll_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬআ")].stop(time=bstack1l1111ll_opy_(), duration=int(attrs.duration)*1000, result=bstack1lll1l11_opy_)
        bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬই"), self.tests[threading.current_thread().current_test_uuid][bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧঈ")])
    def bstack111lllll_opy_(self, attrs):
        bstack1llll1l1_opy_ = {
            bstack1lllll1l_opy_ (u"ࠬ࡯ࡤࠨউ"): uuid4().__str__(),
            bstack1lllll1l_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧঊ"): attrs.keyword,
            bstack1lllll1l_opy_ (u"ࠧࡴࡶࡨࡴࡤࡧࡲࡨࡷࡰࡩࡳࡺࠧঋ"): [],
            bstack1lllll1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭ঌ"): attrs.name,
            bstack1lllll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭঍"): bstack1l1111ll_opy_(),
            bstack1lllll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ঎"): bstack1lllll1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬএ"),
            bstack1lllll1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪঐ"): bstack1lllll1l_opy_ (u"࠭ࠧ঑")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ঒")].add_step(bstack1llll1l1_opy_)
        threading.current_thread().current_step_uuid = bstack1llll1l1_opy_[bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫও")]
    def bstack11l11111_opy_(self, attrs):
        current_test_id = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ঔ"), None)
        current_step_uuid = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧক"), None)
        bstack11l111ll_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=attrs.status.name, exception=exception, bstack1lll11l1_opy_=[bstack11l111ll_opy_])
        self.tests[current_test_id][bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧখ")].bstack1lll1ll1_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1lll1l11_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l1l111_opy_(self, name, attrs):
        try:
            bstack11l11lll_opy_ = uuid4().__str__()
            self.tests[bstack11l11lll_opy_] = {}
            self.bstack1l11111l_opy_.start()
            scopes = []
            driver = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫগ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1lllll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫঘ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11lll_opy_)
            if name in [bstack1lllll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦঙ"), bstack1lllll1l_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦচ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1lllll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥছ"), bstack1lllll1l_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠥজ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1lllll1l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬঝ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l11llll_opy_(
                name=name,
                uuid=bstack11l11lll_opy_,
                started_at=bstack1l1111ll_opy_(),
                file_path=file_path,
                framework=bstack1lllll1l_opy_ (u"ࠧࡈࡥࡩࡣࡹࡩࠧঞ"),
                bstack11lll111_opy_=bstack1ll1l1l1_opy_.bstack1ll111l1_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1lllll1l_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢট"),
                hook_type=name
            )
            self.tests[bstack11l11lll_opy_][bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡡࡵࡣࠥঠ")] = hook_data
            current_test_id = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠣࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠧড"), None)
            if current_test_id:
                hook_data.bstack11l1l1l1_opy_(current_test_id)
            if name == bstack1lllll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨঢ"):
                threading.current_thread().before_all_hook_uuid = bstack11l11lll_opy_
            threading.current_thread().current_hook_uuid = bstack11l11lll_opy_
            bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"ࠥࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠦণ"), hook_data)
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࠠࡩࡱࡲ࡯ࠥ࡫ࡶࡦࡰࡷࡷ࠱ࠦࡨࡰࡱ࡮ࠤࡳࡧ࡭ࡦ࠼ࠣࠩࡸ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠦࡵࠥত"), name, e)
    def bstack11l11l1l_opy_(self, attrs):
        bstack1l11ll1l_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩথ"), None)
        hook_data = self.tests[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩদ")]
        status = bstack1lllll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢধ")
        exception = None
        bstack11l111ll_opy_ = None
        if hook_data.name == bstack1lllll1l_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠦন"):
            self.bstack1l11111l_opy_.reset()
            bstack111llll1_opy_ = self.tests[bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ঩"), None)][bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭প")].result.result
            if bstack111llll1_opy_ == bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦফ"):
                if attrs.hook_failures == 1:
                    status = bstack1lllll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧব")
                elif attrs.hook_failures == 2:
                    status = bstack1lllll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨভ")
            elif attrs.aborted:
                status = bstack1lllll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢম")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1lllll1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬয") and attrs.hook_failures == 1:
                status = bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤর")
            elif hasattr(attrs, bstack1lllll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪ঱")) and attrs.error_message:
                status = bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦল")
            bstack11l111ll_opy_, exception = self._11l1111l_opy_(attrs)
        bstack1lll1l11_opy_ = Result(result=status, exception=exception, bstack1lll11l1_opy_=[bstack11l111ll_opy_])
        hook_data.stop(time=bstack1l1111ll_opy_(), duration=0, result=bstack1lll1l11_opy_)
        bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ঳"), self.tests[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ঴")])
        threading.current_thread().current_hook_uuid = None
    def _11l1111l_opy_(self, attrs):
        try:
            import traceback
            bstack111lll1l_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l111ll_opy_ = bstack111lll1l_opy_[-1] if bstack111lll1l_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࠦ঵"))
            bstack11l111ll_opy_ = None
            exception = None
        return bstack11l111ll_opy_, exception