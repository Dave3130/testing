# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll1111l11_opy_ import bstack1ll1ll1ll1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack11lll1l1l_opy_ import bstack1l1llllll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1l1ll_opy_,
    bstack1lll1ll1lll_opy_,
    bstack1lll1ll11ll_opy_,
    bstack1ll1111l11l_opy_,
    bstack1ll1111lll1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll11l1l111_opy_
from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11lll11_opy_ import bstack1lll11ll1ll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l11l_opy_ import bstack1ll11l11111_opy_
from bstack_utils.bstack1l111111_opy_ import bstack1l1l11l1_opy_
bstack1ll11ll11ll_opy_ = bstack1ll11l1l111_opy_()
bstack1l1llll11ll_opy_ = 1.0
bstack1ll111lll11_opy_ = bstack11l111_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᕙ")
bstack11llll1l111_opy_ = bstack11l111_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᕚ")
bstack11llll1l11l_opy_ = bstack11l111_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᕛ")
bstack11llll1l1l1_opy_ = bstack11l111_opy_ (u"ࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦᕜ")
bstack11llll1l1ll_opy_ = bstack11l111_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣᕝ")
_1ll1l11l111_opy_ = set()
class bstack1l1l111111l_opy_(TestFramework):
    bstack1ll11111l1l_opy_ = bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᕞ")
    bstack1ll1ll11111_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࠤᕟ")
    bstack1ll1l11ll11_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᕠ")
    bstack1ll111l1ll1_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣᕡ")
    bstack1ll11l1llll_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥᕢ")
    bstack1ll11lll11l_opy_: bool
    bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_  = None
    bstack1lllllllll1_opy_ = None
    bstack1ll11111ll1_opy_ = [
        bstack1lll1l1l1ll_opy_.BEFORE_ALL,
        bstack1lll1l1l1ll_opy_.AFTER_ALL,
        bstack1lll1l1l1ll_opy_.BEFORE_EACH,
        bstack1lll1l1l1ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1llllll11_opy_: Dict[str, str],
        bstack1ll111ll1ll_opy_: List[str]=[bstack11l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᕣ")],
        bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_=None,
        bstack1lllllllll1_opy_=None
    ):
        super().__init__(bstack1ll111ll1ll_opy_, bstack1l1llllll11_opy_, bstack1lll11lll11_opy_)
        self.bstack1ll11lll11l_opy_ = any(bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᕤ") in item.lower() for item in bstack1ll111ll1ll_opy_)
        self.bstack1lllllllll1_opy_ = bstack1lllllllll1_opy_
    def track_event(
        self,
        context: bstack1ll1111l11l_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        test_hook_state: bstack1lll1ll11ll_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1l1ll_opy_.TEST or test_framework_state in bstack1l1l111111l_opy_.bstack1ll11111ll1_opy_:
            bstack1l1llllll1l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1l1ll_opy_.NONE:
            self.logger.warning(bstack11l111_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧࡧࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࠦᕥ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠦࠧᕦ"))
            return
        if not self.bstack1ll11lll11l_opy_:
            self.logger.warning(bstack11l111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡂࠨᕧ") + str(str(self.bstack1ll111ll1ll_opy_)) + bstack11l111_opy_ (u"ࠨࠢᕨ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕩ") + str(kwargs) + bstack11l111_opy_ (u"ࠣࠤᕪ"))
            return
        instance = self.__1ll1l1ll1ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡤࡶ࡬ࡹ࠽ࠣᕫ") + str(args) + bstack11l111_opy_ (u"ࠥࠦᕬ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l111111l_opy_.bstack1ll11111ll1_opy_ and test_hook_state == bstack1lll1ll11ll_opy_.PRE:
                bstack1ll11l1lll1_opy_ = bstack1lllll111l1_opy_.bstack1ll1l1l111l_opy_(EVENTS.bstack1l11lllll_opy_.value)
                name = str(EVENTS.bstack1l11lllll_opy_.name)+bstack11l111_opy_ (u"ࠦ࠿ࠨᕭ")+str(test_framework_state.name)
                TestFramework.bstack1ll11lllll1_opy_(instance, name, bstack1ll11l1lll1_opy_)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲࠡࡲࡵࡩ࠿ࠦࡻࡾࠤᕮ").format(e))
        try:
            if not TestFramework.bstack1lllll11l1l_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_) and test_hook_state == bstack1lll1ll11ll_opy_.PRE:
                test = bstack1l1l111111l_opy_.__1ll1l11lll1_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l111_opy_ (u"ࠨ࡬ࡰࡣࡧࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᕯ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠢࠣᕰ"))
            if test_framework_state == bstack1lll1l1l1ll_opy_.TEST:
                if test_hook_state == bstack1lll1ll11ll_opy_.PRE and not TestFramework.bstack1lllll11l1l_opy_(instance, TestFramework.bstack1ll11l11l1l_opy_):
                    TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11l11l1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l111_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡷࡹࡧࡲࡵࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᕱ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠤࠥᕲ"))
                elif test_hook_state == bstack1lll1ll11ll_opy_.POST and not TestFramework.bstack1lllll11l1l_opy_(instance, TestFramework.bstack1ll11ll111l_opy_):
                    TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11ll111l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l111_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲࡫࡮ࡥࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᕳ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠦࠧᕴ"))
            elif test_framework_state == bstack1lll1l1l1ll_opy_.LOG and test_hook_state == bstack1lll1ll11ll_opy_.POST:
                bstack1l1l111111l_opy_.__1ll111l1l1l_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1l1ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll11ll_opy_.POST:
                self.__1ll11llll1l_opy_(instance, *args)
                self.__1ll11111l11_opy_(instance)
            elif test_framework_state in bstack1l1l111111l_opy_.bstack1ll11111ll1_opy_:
                self.__1ll111ll111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᕵ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠨࠢᕶ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111ll1l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l111111l_opy_.bstack1ll11111ll1_opy_ and test_hook_state == bstack1lll1ll11ll_opy_.POST:
                name = str(EVENTS.bstack1l11lllll_opy_.name)+bstack11l111_opy_ (u"ࠢ࠻ࠤᕷ")+str(test_framework_state.name)
                bstack1ll11l1lll1_opy_ = TestFramework.bstack1ll11l111l1_opy_(instance, name)
                bstack1lllll111l1_opy_.end(EVENTS.bstack1l11lllll_opy_.value, bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᕸ"), bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᕹ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᕺ").format(e))
    def bstack1ll1l1l1l11_opy_(self):
        return self.bstack1ll11lll11l_opy_
    def __1ll11l1l1l1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣᕻ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1lllll111_opy_(rep, [bstack11l111_opy_ (u"ࠧࡽࡨࡦࡰࠥᕼ"), bstack11l111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᕽ"), bstack11l111_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᕾ"), bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᕿ"), bstack11l111_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠥᖀ"), bstack11l111_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤᖁ")])
        return None
    def __1ll11llll1l_opy_(self, instance: bstack1lll1ll1lll_opy_, *args):
        result = self.__1ll11l1l1l1_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l1111_opy_ = None
        if result.get(bstack11l111_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖂ"), None) == bstack11l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᖃ") and len(args) > 1 and getattr(args[1], bstack11l111_opy_ (u"ࠨࡥࡹࡥ࡬ࡲ࡫ࡵࠢᖄ"), None) is not None:
            failure = [{bstack11l111_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᖅ"): [args[1].excinfo.exconly(), result.get(bstack11l111_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢᖆ"), None)]}]
            bstack11111l1111_opy_ = bstack11l111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᖇ") if bstack11l111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨᖈ") in getattr(args[1].excinfo, bstack11l111_opy_ (u"ࠦࡹࡿࡰࡦࡰࡤࡱࡪࠨᖉ"), bstack11l111_opy_ (u"ࠧࠨᖊ")) else bstack11l111_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᖋ")
        bstack1ll111lll1l_opy_ = result.get(bstack11l111_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖌ"), TestFramework.bstack1ll11llllll_opy_)
        if bstack1ll111lll1l_opy_ != TestFramework.bstack1ll11llllll_opy_:
            TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1lllll1l1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l1lll1l_opy_(instance, {
            TestFramework.bstack1llll11llll_opy_: failure,
            TestFramework.bstack1ll111111l1_opy_: bstack11111l1111_opy_,
            TestFramework.bstack1llll1111l1_opy_: bstack1ll111lll1l_opy_,
        })
    def __1ll1l1ll1ll_opy_(
        self,
        context: bstack1ll1111l11l_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        test_hook_state: bstack1lll1ll11ll_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1l1ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11lll111_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11111111_opy_ bstack1ll111l111l_opy_ this to be bstack11l111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖍ")
            if test_framework_state == bstack1lll1l1l1ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll111ll11l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1l1ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᖎ"), None), bstack11l111_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᖏ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖐ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111llll1_opy_(target) if target else None
        return instance
    def __1ll111ll111_opy_(
        self,
        instance: bstack1lll1ll1lll_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        test_hook_state: bstack1lll1ll11ll_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1lll11_opy_ = TestFramework.get_state(instance, bstack1l1l111111l_opy_.bstack1ll1ll11111_opy_, {})
        if not key in bstack1ll1l1lll11_opy_:
            bstack1ll1l1lll11_opy_[key] = []
        bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1l1l111111l_opy_.bstack1ll1l11ll11_opy_, {})
        if not key in bstack1ll111111ll_opy_:
            bstack1ll111111ll_opy_[key] = []
        bstack1ll111l11l1_opy_ = {
            bstack1l1l111111l_opy_.bstack1ll1ll11111_opy_: bstack1ll1l1lll11_opy_,
            bstack1l1l111111l_opy_.bstack1ll1l11ll11_opy_: bstack1ll111111ll_opy_,
        }
        if test_hook_state == bstack1lll1ll11ll_opy_.PRE:
            hook = {
                bstack11l111_opy_ (u"ࠧࡱࡥࡺࠤᖑ"): key,
                TestFramework.bstack1ll1l1l11l1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l1l1lll_opy_: TestFramework.bstack1ll1l1lllll_opy_,
                TestFramework.bstack1ll1l11llll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11lll1ll_opy_: [],
                TestFramework.bstack1ll1l111ll1_opy_: args[1] if len(args) > 1 else bstack11l111_opy_ (u"࠭ࠧᖒ"),
                TestFramework.bstack1ll1111l1ll_opy_: bstack1ll11l11111_opy_.bstack1ll11l11l11_opy_()
            }
            bstack1ll1l1lll11_opy_[key].append(hook)
            bstack1ll111l11l1_opy_[bstack1l1l111111l_opy_.bstack1ll111l1ll1_opy_] = key
        elif test_hook_state == bstack1lll1ll11ll_opy_.POST:
            bstack1ll11ll11l1_opy_ = bstack1ll1l1lll11_opy_.get(key, [])
            hook = bstack1ll11ll11l1_opy_.pop() if bstack1ll11ll11l1_opy_ else None
            if hook:
                result = self.__1ll11l1l1l1_opy_(*args)
                if result:
                    bstack1ll11l1ll1l_opy_ = result.get(bstack11l111_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖓ"), TestFramework.bstack1ll1l1lllll_opy_)
                    if bstack1ll11l1ll1l_opy_ != TestFramework.bstack1ll1l1lllll_opy_:
                        hook[TestFramework.bstack1ll1l1l1lll_opy_] = bstack1ll11l1ll1l_opy_
                hook[TestFramework.bstack1l1lllllll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1111l1ll_opy_]= bstack1ll11l11111_opy_.bstack1ll11l11l11_opy_()
                self.bstack1ll11ll1111_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1111llll_opy_, [])
                if logs: self.bstack1ll11l1l1ll_opy_(instance, logs)
                bstack1ll111111ll_opy_[key].append(hook)
                bstack1ll111l11l1_opy_[bstack1l1l111111l_opy_.bstack1ll11l1llll_opy_] = key
        TestFramework.bstack1ll1l1lll1l_opy_(instance, bstack1ll111l11l1_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡩࡱࡲ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼ࡭ࡨࡽࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࡀࡿ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࢁࠥ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡃࠢᖔ") + str(bstack1ll111111ll_opy_) + bstack11l111_opy_ (u"ࠤࠥᖕ"))
    def __1ll11lll111_opy_(
        self,
        context: bstack1ll1111l11l_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        test_hook_state: bstack1lll1ll11ll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1lllll111_opy_(args[0], [bstack11l111_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᖖ"), bstack11l111_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᖗ"), bstack11l111_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᖘ"), bstack11l111_opy_ (u"ࠨࡩࡥࡵࠥᖙ"), bstack11l111_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤᖚ"), bstack11l111_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣᖛ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l111_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᖜ")) else fixturedef.get(bstack11l111_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᖝ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l111_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࠤᖞ")) else None
        node = request.node if hasattr(request, bstack11l111_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᖟ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖠ")) else None
        baseid = fixturedef.get(bstack11l111_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢᖡ"), None) or bstack11l111_opy_ (u"ࠣࠤᖢ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l111_opy_ (u"ࠤࡢࡴࡾ࡬ࡵ࡯ࡥ࡬ࡸࡪࡳࠢᖣ")):
            target = bstack1l1l111111l_opy_.__1l1llll1l11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l111_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᖤ")) else None
            if target and not TestFramework.bstack1ll111llll1_opy_(target):
                self.__1ll111ll11l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦ࡮ࡰࡦࡨࡁࢀࡴ࡯ࡥࡧࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᖥ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠧࠨᖦ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦᖧ") + str(target) + bstack11l111_opy_ (u"ࠢࠣᖨ"))
            return None
        instance = TestFramework.bstack1ll111llll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡣࡣࡶࡩ࡮ࡪ࠽ࡼࡤࡤࡷࡪ࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥᖩ") + str(target) + bstack11l111_opy_ (u"ࠤࠥᖪ"))
            return None
        bstack1ll111l1111_opy_ = TestFramework.get_state(instance, bstack1l1l111111l_opy_.bstack1ll11111l1l_opy_, {})
        if os.getenv(bstack11l111_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡉࡍ࡝࡚ࡕࡓࡇࡖࠦᖫ"), bstack11l111_opy_ (u"ࠦ࠶ࠨᖬ")) == bstack11l111_opy_ (u"ࠧ࠷ࠢᖭ"):
            bstack1ll1l11l1l1_opy_ = bstack11l111_opy_ (u"ࠨ࠺ࠣᖮ").join((scope, fixturename))
            bstack1ll11l1111l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll111l1l11_opy_ = {
                bstack11l111_opy_ (u"ࠢ࡬ࡧࡼࠦᖯ"): bstack1ll1l11l1l1_opy_,
                bstack11l111_opy_ (u"ࠣࡶࡤ࡫ࡸࠨᖰ"): bstack1l1l111111l_opy_.__1ll1l11l1ll_opy_(request.node),
                bstack11l111_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࠥᖱ"): fixturedef,
                bstack11l111_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᖲ"): scope,
                bstack11l111_opy_ (u"ࠦࡹࡿࡰࡦࠤᖳ"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll11ll_opy_.POST and callable(getattr(args[-1], bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᖴ"), None)):
                    bstack1ll111l1l11_opy_[bstack11l111_opy_ (u"ࠨࡴࡺࡲࡨࠦᖵ")] = TestFramework.bstack1ll1l1111ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll11ll_opy_.PRE:
                bstack1ll111l1l11_opy_[bstack11l111_opy_ (u"ࠢࡶࡷ࡬ࡨࠧᖶ")] = uuid4().__str__()
                bstack1ll111l1l11_opy_[bstack1l1l111111l_opy_.bstack1ll1l11llll_opy_] = bstack1ll11l1111l_opy_
            elif test_hook_state == bstack1lll1ll11ll_opy_.POST:
                bstack1ll111l1l11_opy_[bstack1l1l111111l_opy_.bstack1l1lllllll1_opy_] = bstack1ll11l1111l_opy_
            if bstack1ll1l11l1l1_opy_ in bstack1ll111l1111_opy_:
                bstack1ll111l1111_opy_[bstack1ll1l11l1l1_opy_].update(bstack1ll111l1l11_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࠤᖷ") + str(bstack1ll111l1111_opy_[bstack1ll1l11l1l1_opy_]) + bstack11l111_opy_ (u"ࠤࠥᖸ"))
            else:
                bstack1ll111l1111_opy_[bstack1ll1l11l1l1_opy_] = bstack1ll111l1l11_opy_
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡾࠢࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࠨᖹ") + str(len(bstack1ll111l1111_opy_)) + bstack11l111_opy_ (u"ࠦࠧᖺ"))
        TestFramework.bstack1lllll111ll_opy_(instance, bstack1l1l111111l_opy_.bstack1ll11111l1l_opy_, bstack1ll111l1111_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࡻ࡭ࡧࡱࠬࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠩࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᖻ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠨࠢᖼ"))
        return instance
    def __1ll111ll11l_opy_(
        self,
        context: bstack1ll1111l11l_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1ll1l_opy_.create_context(target)
        ob = bstack1lll1ll1lll_opy_(ctx, self.bstack1ll111ll1ll_opy_, self.bstack1l1llllll11_opy_, test_framework_state)
        TestFramework.bstack1ll1l1lll1l_opy_(ob, {
            TestFramework.bstack1lll1llll1l_opy_: context.test_framework_name,
            TestFramework.bstack1llll111lll_opy_: context.test_framework_version,
            TestFramework.bstack1l1llllllll_opy_: [],
            bstack1l1l111111l_opy_.bstack1ll11111l1l_opy_: {},
            bstack1l1l111111l_opy_.bstack1ll1l11ll11_opy_: {},
            bstack1l1l111111l_opy_.bstack1ll1ll11111_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll111ll_opy_(ob, TestFramework.bstack1ll1l1ll11l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll111ll_opy_(ob, TestFramework.bstack1111111l1l_opy_, context.platform_index)
        TestFramework.bstack1lll1l11lll_opy_[ctx.id] = ob
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡥࡷࡼ࠳࡯ࡤ࠾ࡽࡦࡸࡽ࠴ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢᖽ") + str(TestFramework.bstack1lll1l11lll_opy_.keys()) + bstack11l111_opy_ (u"ࠣࠤᖾ"))
        return ob
    def bstack1ll111l1lll_opy_(self, instance: bstack1lll1ll1lll_opy_, bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_]):
        bstack1ll1111111l_opy_ = (
            bstack1l1l111111l_opy_.bstack1ll111l1ll1_opy_
            if bstack1llll1ll1ll_opy_[1] == bstack1lll1ll11ll_opy_.PRE
            else bstack1l1l111111l_opy_.bstack1ll11l1llll_opy_
        )
        hook = bstack1l1l111111l_opy_.bstack1ll1l1llll1_opy_(instance, bstack1ll1111111l_opy_)
        entries = hook.get(TestFramework.bstack1ll11lll1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1l1llllllll_opy_, []))
        return entries
    def bstack1l1lllll11l_opy_(self, instance: bstack1lll1ll1lll_opy_, bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_]):
        bstack1ll1111111l_opy_ = (
            bstack1l1l111111l_opy_.bstack1ll111l1ll1_opy_
            if bstack1llll1ll1ll_opy_[1] == bstack1lll1ll11ll_opy_.PRE
            else bstack1l1l111111l_opy_.bstack1ll11l1llll_opy_
        )
        bstack1l1l111111l_opy_.bstack1ll111lllll_opy_(instance, bstack1ll1111111l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1l1llllllll_opy_, []).clear()
    def bstack1ll11ll1111_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᖿ")
        global _1ll1l11l111_opy_
        platform_index = os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᗀ")]
        bstack1ll1l111l1l_opy_ = os.path.join(bstack1ll11ll11ll_opy_, (bstack1ll111lll11_opy_ + str(platform_index)), bstack11llll1l1l1_opy_)
        if not os.path.exists(bstack1ll1l111l1l_opy_) or not os.path.isdir(bstack1ll1l111l1l_opy_):
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࡴࠢࡷࡳࠥࡶࡲࡰࡥࡨࡷࡸࠦࡻࡾࠤᗁ").format(bstack1ll1l111l1l_opy_))
            return
        logs = hook.get(bstack11l111_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᗂ"), [])
        with os.scandir(bstack1ll1l111l1l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l11l111_opy_:
                    self.logger.info(bstack11l111_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᗃ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l111_opy_ (u"ࠢࠣᗄ")
                    log_entry = bstack1ll1111lll1_opy_(
                        kind=bstack11l111_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗅ"),
                        message=bstack11l111_opy_ (u"ࠤࠥᗆ"),
                        level=bstack11l111_opy_ (u"ࠥࠦᗇ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l11lll_opy_=entry.stat().st_size,
                        bstack1ll1l1111l1_opy_=bstack11l111_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᗈ"),
                        bstack11ll11_opy_=os.path.abspath(entry.path),
                        bstack1ll1111l111_opy_=hook.get(TestFramework.bstack1ll1l1l11l1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l11l111_opy_.add(abs_path)
        platform_index = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᗉ")]
        bstack1ll1l1l11ll_opy_ = os.path.join(bstack1ll11ll11ll_opy_, (bstack1ll111lll11_opy_ + str(platform_index)), bstack11llll1l1l1_opy_, bstack11llll1l1ll_opy_)
        if not os.path.exists(bstack1ll1l1l11ll_opy_) or not os.path.isdir(bstack1ll1l1l11ll_opy_):
            self.logger.info(bstack11l111_opy_ (u"ࠨࡎࡰࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡩࡳࡺࡴࡤࠡࡣࡷ࠾ࠥࢁࡽࠣᗊ").format(bstack1ll1l1l11ll_opy_))
        else:
            self.logger.info(bstack11l111_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡨࡵࡳࡲࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠼ࠣࡿࢂࠨᗋ").format(bstack1ll1l1l11ll_opy_))
            with os.scandir(bstack1ll1l1l11ll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l11l111_opy_:
                        self.logger.info(bstack11l111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᗌ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l111_opy_ (u"ࠤࠥᗍ")
                        log_entry = bstack1ll1111lll1_opy_(
                            kind=bstack11l111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᗎ"),
                            message=bstack11l111_opy_ (u"ࠦࠧᗏ"),
                            level=bstack11l111_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᗐ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l11lll_opy_=entry.stat().st_size,
                            bstack1ll1l1111l1_opy_=bstack11l111_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᗑ"),
                            bstack11ll11_opy_=os.path.abspath(entry.path),
                            bstack1ll11ll1l11_opy_=hook.get(TestFramework.bstack1ll1l1l11l1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l11l111_opy_.add(abs_path)
        hook[bstack11l111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᗒ")] = logs
    def bstack1ll11l1l1ll_opy_(
        self,
        bstack1ll1l111111_opy_: bstack1lll1ll1lll_opy_,
        entries: List[bstack1ll1111lll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧᗓ"))
        req.platform_index = TestFramework.get_state(bstack1ll1l111111_opy_, TestFramework.bstack1111111l1l_opy_)
        req.execution_context.hash = str(bstack1ll1l111111_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l111111_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l111111_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l111111_opy_, TestFramework.bstack1lll1llll1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l111111_opy_, TestFramework.bstack1llll111lll_opy_)
            log_entry.uuid = entry.bstack1ll1111l111_opy_
            log_entry.test_framework_state = bstack1ll1l111111_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᗔ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11l111_opy_ (u"ࠥࠦᗕ")
            if entry.kind == bstack11l111_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᗖ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l11lll_opy_
                log_entry.file_path = entry.bstack11ll11_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1lll1l1ll1_opy_ = datetime.now()
            try:
                self.bstack1lllllllll1_opy_.LogCreatedEvent(req)
                bstack1ll1l111111_opy_.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᗗ"), datetime.now() - bstack1lll1l1ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡾࢁࠧᗘ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lll11_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def __1ll11111l11_opy_(self, instance) -> None:
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡑࡵࡡࡥࡵࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࡳࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡳࡧࡤࡸࡪࡹࠠࡢࠢࡧ࡭ࡨࡺࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡹ࡫ࡳࡵࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡦࡳࡱࡰࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡵࡴࡶࡲࡱ࡙ࡧࡧࡎࡣࡱࡥ࡬࡫ࡲࠡࡣࡱࡨࠥࡻࡰࡥࡣࡷࡩࡸࠦࡴࡩࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡹࡴࡢࡶࡨࠤࡺࡹࡩ࡯ࡩࠣࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᗙ")
        bstack1ll111l11l1_opy_ = {bstack11l111_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠥᗚ"): bstack1ll11l11111_opy_.bstack1ll11l11l11_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1l1lll1l_opy_(instance, bstack1ll111l11l1_opy_)
    @staticmethod
    def bstack1ll1l1llll1_opy_(instance: bstack1lll1ll1lll_opy_, bstack1ll1111111l_opy_: str):
        bstack1ll1l1l1ll1_opy_ = (
            bstack1l1l111111l_opy_.bstack1ll1l11ll11_opy_
            if bstack1ll1111111l_opy_ == bstack1l1l111111l_opy_.bstack1ll11l1llll_opy_
            else bstack1l1l111111l_opy_.bstack1ll1ll11111_opy_
        )
        bstack1ll1l11111l_opy_ = TestFramework.get_state(instance, bstack1ll1111111l_opy_, None)
        bstack1ll1l11ll1l_opy_ = TestFramework.get_state(instance, bstack1ll1l1l1ll1_opy_, None) if bstack1ll1l11111l_opy_ else None
        return (
            bstack1ll1l11ll1l_opy_[bstack1ll1l11111l_opy_][-1]
            if isinstance(bstack1ll1l11ll1l_opy_, dict) and len(bstack1ll1l11ll1l_opy_.get(bstack1ll1l11111l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll111lllll_opy_(instance: bstack1lll1ll1lll_opy_, bstack1ll1111111l_opy_: str):
        hook = bstack1l1l111111l_opy_.bstack1ll1l1llll1_opy_(instance, bstack1ll1111111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11lll1ll_opy_, []).clear()
    @staticmethod
    def __1ll111l1l1l_opy_(instance: bstack1lll1ll1lll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l111_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢᗛ"), None)):
            return
        if os.getenv(bstack11l111_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢᗜ"), bstack11l111_opy_ (u"ࠦ࠶ࠨᗝ")) != bstack11l111_opy_ (u"ࠧ࠷ࠢᗞ"):
            bstack1l1l111111l_opy_.logger.warning(bstack11l111_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣᗟ"))
            return
        bstack1l1llll1l1l_opy_ = {
            bstack11l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᗠ"): (bstack1l1l111111l_opy_.bstack1ll111l1ll1_opy_, bstack1l1l111111l_opy_.bstack1ll1ll11111_opy_),
            bstack11l111_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᗡ"): (bstack1l1l111111l_opy_.bstack1ll11l1llll_opy_, bstack1l1l111111l_opy_.bstack1ll1l11ll11_opy_),
        }
        for when in (bstack11l111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᗢ"), bstack11l111_opy_ (u"ࠥࡧࡦࡲ࡬ࠣᗣ"), bstack11l111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᗤ")):
            bstack1ll11llll11_opy_ = args[1].get_records(when)
            if not bstack1ll11llll11_opy_:
                continue
            records = [
                bstack1ll1111lll1_opy_(
                    kind=TestFramework.bstack1ll1l1l1111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l111_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣᗥ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l111_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢᗦ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11llll11_opy_
                if isinstance(getattr(r, bstack11l111_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣᗧ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l11ll1_opy_, bstack1ll1l1l1ll1_opy_ = bstack1l1llll1l1l_opy_.get(when, (None, None))
            bstack1ll1111l1l1_opy_ = TestFramework.get_state(instance, bstack1ll11l11ll1_opy_, None) if bstack1ll11l11ll1_opy_ else None
            bstack1ll1l11ll1l_opy_ = TestFramework.get_state(instance, bstack1ll1l1l1ll1_opy_, None) if bstack1ll1111l1l1_opy_ else None
            if isinstance(bstack1ll1l11ll1l_opy_, dict) and len(bstack1ll1l11ll1l_opy_.get(bstack1ll1111l1l1_opy_, [])) > 0:
                hook = bstack1ll1l11ll1l_opy_[bstack1ll1111l1l1_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11lll1ll_opy_ in hook:
                    hook[TestFramework.bstack1ll11lll1ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1l1llllllll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l11lll1_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l111111l_opy_.__1l1llll1l11_opy_(test.location) if hasattr(test, bstack11l111_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᗨ")) else getattr(test, bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗩ"), None)
        test_name = test.name if hasattr(test, bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᗪ")) else None
        bstack1ll11l1ll11_opy_ = test.fspath.strpath if hasattr(test, bstack11l111_opy_ (u"ࠦ࡫ࡹࡰࡢࡶ࡫ࠦᗫ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll11l1ll11_opy_:
            return None
        code = None
        if hasattr(test, bstack11l111_opy_ (u"ࠧࡵࡢ࡫ࠤᗬ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll11lll_opy_ = []
        try:
            bstack11llll11lll_opy_ = bstack1l1l11l1_opy_.bstack1lllll11_opy_(test)
        except:
            bstack1l1l111111l_opy_.logger.warning(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡧࡶࡸࠥࡹࡣࡰࡲࡨࡷ࠱ࠦࡴࡦࡵࡷࠤࡸࡩ࡯ࡱࡧࡶࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡸࡥࡴࡱ࡯ࡺࡪࡪࠠࡪࡰࠣࡇࡑࡏࠢᗭ"))
        return {
            TestFramework.bstack1lll1l111l1_opy_: uuid4().__str__(),
            TestFramework.bstack1l1llll1ll1_opy_: test_id,
            TestFramework.bstack1ll11l111ll_opy_: test_name,
            TestFramework.bstack1ll11ll1lll_opy_: getattr(test, bstack11l111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗮ"), None),
            TestFramework.bstack1ll111l11ll_opy_: bstack1ll11l1ll11_opy_,
            TestFramework.bstack1l1llll1lll_opy_: bstack1l1l111111l_opy_.__1ll1l11l1ll_opy_(test),
            TestFramework.bstack1ll1l111lll_opy_: code,
            TestFramework.bstack1llll1111l1_opy_: TestFramework.bstack1ll11llllll_opy_,
            TestFramework.bstack1lll111llll_opy_: test_id,
            TestFramework.bstack1l11111lll1_opy_: bstack11llll11lll_opy_
        }
    @staticmethod
    def __1ll1l11l1ll_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11l111_opy_ (u"ࠣࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸࠨᗯ"), [])
            markers.extend([getattr(m, bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᗰ"), None) for m in own_markers if getattr(m, bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᗱ"), None)])
            current = getattr(current, bstack11l111_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᗲ"), None)
        return markers
    @staticmethod
    def __1l1llll1l11_opy_(location):
        return bstack11l111_opy_ (u"ࠧࡀ࠺ࠣᗳ").join(filter(lambda x: isinstance(x, str), location))