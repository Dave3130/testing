# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1ll1lll1111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1lll1ll_opy_ import bstack1ll1111l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll111lll_opy_,
    bstack1lll1lll1l1_opy_,
    bstack1lll1lll11l_opy_,
    bstack1l1llllllll_opy_,
    bstack1ll111lll11_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll11llllll_opy_
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1ll1l_opy_ import bstack1ll1l1ll111_opy_
from bstack_utils.bstack1l1111l1_opy_ import bstack1ll1l1ll_opy_
bstack1ll111l1l1l_opy_ = bstack1ll11llllll_opy_()
bstack1ll111111l1_opy_ = 1.0
bstack1ll1l1l1lll_opy_ = bstack111111l_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᕟ")
bstack11llll1l1l1_opy_ = bstack111111l_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᕠ")
bstack11llll1ll11_opy_ = bstack111111l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᕡ")
bstack11llll1ll1l_opy_ = bstack111111l_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥᕢ")
bstack11llll1l11l_opy_ = bstack111111l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢᕣ")
_1ll111l1ll1_opy_ = set()
class bstack1l1l1l111ll_opy_(TestFramework):
    bstack1ll1l1lll1l_opy_ = bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᕤ")
    bstack1ll1l11ll11_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣᕥ")
    bstack1ll111l11l1_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥᕦ")
    bstack1ll11l1111l_opy_ = bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪࠢᕧ")
    bstack1ll1l111lll_opy_ = bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᕨ")
    bstack1ll1111lll1_opy_: bool
    bstack1lll11lllll_opy_: bstack1lll11llll1_opy_  = None
    bstack111111111l_opy_ = None
    bstack1ll1111ll1l_opy_ = [
        bstack1llll111lll_opy_.BEFORE_ALL,
        bstack1llll111lll_opy_.AFTER_ALL,
        bstack1llll111lll_opy_.BEFORE_EACH,
        bstack1llll111lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11lll11l_opy_: Dict[str, str],
        bstack1ll11l11ll1_opy_: List[str]=[bstack111111l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᕩ")],
        bstack1lll11lllll_opy_: bstack1lll11llll1_opy_=None,
        bstack111111111l_opy_=None
    ):
        super().__init__(bstack1ll11l11ll1_opy_, bstack1ll11lll11l_opy_, bstack1lll11lllll_opy_)
        self.bstack1ll1111lll1_opy_ = any(bstack111111l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᕪ") in item.lower() for item in bstack1ll11l11ll1_opy_)
        self.bstack111111111l_opy_ = bstack111111111l_opy_
    def track_event(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll111lll_opy_.TEST or test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1111ll1l_opy_:
            bstack1ll1111l1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll111lll_opy_.NONE:
            self.logger.warning(bstack111111l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࠥᕫ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠥࠦᕬ"))
            return
        if not self.bstack1ll1111lll1_opy_:
            self.logger.warning(bstack111111l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡁࠧᕭ") + str(str(self.bstack1ll11l11ll1_opy_)) + bstack111111l_opy_ (u"ࠧࠨᕮ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack111111l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᕯ") + str(kwargs) + bstack111111l_opy_ (u"ࠢࠣᕰ"))
            return
        instance = self.__1ll1l1l1l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࠢᕱ") + str(args) + bstack111111l_opy_ (u"ࠤࠥᕲ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1111ll1l_opy_ and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack1ll1111ll_opy_.value)
                name = str(EVENTS.bstack1ll1111ll_opy_.name)+bstack111111l_opy_ (u"ࠥ࠾ࠧᕳ")+str(test_framework_state.name)
                TestFramework.bstack1ll111l1111_opy_(instance, name, bstack1ll1l1ll1ll_opy_)
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸࠠࡱࡴࡨ࠾ࠥࢁࡽࠣᕴ").format(e))
        try:
            if not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_) and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                test = bstack1l1l1l111ll_opy_.__1ll1l11llll_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack111111l_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᕵ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠨࠢᕶ"))
            if test_framework_state == bstack1llll111lll_opy_.TEST:
                if test_hook_state == bstack1lll1lll11l_opy_.PRE and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll111l1l11_opy_):
                    TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll111l1l11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack111111l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᕷ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠣࠤᕸ"))
                elif test_hook_state == bstack1lll1lll11l_opy_.POST and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_):
                    TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack111111l_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᕹ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠥࠦᕺ"))
            elif test_framework_state == bstack1llll111lll_opy_.LOG and test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1l1l1l111ll_opy_.__1ll1l111l1l_opy_(instance, *args)
            elif test_framework_state == bstack1llll111lll_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll11l_opy_.POST:
                self.__1l1lllll1l1_opy_(instance, *args)
                self.__1ll111ll1l1_opy_(instance)
            elif test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1111ll1l_opy_:
                self.__1ll11llll11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᕻ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠧࠨᕼ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l11l1l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1111ll1l_opy_ and test_hook_state == bstack1lll1lll11l_opy_.POST:
                name = str(EVENTS.bstack1ll1111ll_opy_.name)+bstack111111l_opy_ (u"ࠨ࠺ࠣᕽ")+str(test_framework_state.name)
                bstack1ll1l1ll1ll_opy_ = TestFramework.bstack1ll111lll1l_opy_(instance, name)
                bstack1llllll1lll_opy_.end(EVENTS.bstack1ll1111ll_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕾ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕿ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᖀ").format(e))
    def bstack1ll1l1lll11_opy_(self):
        return self.bstack1ll1111lll1_opy_
    def __1ll11ll1l1l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack111111l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᖁ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11111l11_opy_(rep, [bstack111111l_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤᖂ"), bstack111111l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᖃ"), bstack111111l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨᖄ"), bstack111111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᖅ"), bstack111111l_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤᖆ"), bstack111111l_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣᖇ")])
        return None
    def __1l1lllll1l1_opy_(self, instance: bstack1lll1lll1l1_opy_, *args):
        result = self.__1ll11ll1l1l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l111l_opy_ = None
        if result.get(bstack111111l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖈ"), None) == bstack111111l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᖉ") and len(args) > 1 and getattr(args[1], bstack111111l_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨᖊ"), None) is not None:
            failure = [{bstack111111l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᖋ"): [args[1].excinfo.exconly(), result.get(bstack111111l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨᖌ"), None)]}]
            bstack11111l111l_opy_ = bstack111111l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᖍ") if bstack111111l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᖎ") in getattr(args[1].excinfo, bstack111111l_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧᖏ"), bstack111111l_opy_ (u"ࠦࠧᖐ")) else bstack111111l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᖑ")
        bstack1ll111l111l_opy_ = result.get(bstack111111l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᖒ"), TestFramework.bstack1ll11llll1l_opy_)
        if bstack1ll111l111l_opy_ != TestFramework.bstack1ll11llll1l_opy_:
            TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l11l111_opy_(instance, {
            TestFramework.bstack1lll1ll11ll_opy_: failure,
            TestFramework.bstack1ll111ll111_opy_: bstack11111l111l_opy_,
            TestFramework.bstack1lll1ll1ll1_opy_: bstack1ll111l111l_opy_,
        })
    def __1ll1l1l1l1l_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll111lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll111llll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll1111_opy_ bstack1ll1ll1111l_opy_ this to be bstack111111l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᖓ")
            if test_framework_state == bstack1llll111lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11111l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll111lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack111111l_opy_ (u"ࠣࡰࡲࡨࡪࠨᖔ"), None), bstack111111l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᖕ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack111111l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᖖ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11ll1lll_opy_(target) if target else None
        return instance
    def __1ll11llll11_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l11lll1_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll1l11ll11_opy_, {})
        if not key in bstack1ll1l11lll1_opy_:
            bstack1ll1l11lll1_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll111l11l1_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll1111ll11_opy_ = {
            bstack1l1l1l111ll_opy_.bstack1ll1l11ll11_opy_: bstack1ll1l11lll1_opy_,
            bstack1l1l1l111ll_opy_.bstack1ll111l11l1_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1lll11l_opy_.PRE:
            hook = {
                bstack111111l_opy_ (u"ࠦࡰ࡫ࡹࠣᖗ"): key,
                TestFramework.bstack1ll1l1111l1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l111ll_opy_: TestFramework.bstack1ll11ll1l11_opy_,
                TestFramework.bstack1ll11lllll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l1l1_opy_: [],
                TestFramework.bstack1ll11l1l111_opy_: args[1] if len(args) > 1 else bstack111111l_opy_ (u"ࠬ࠭ᖘ"),
                TestFramework.bstack1ll1l1ll1l1_opy_: bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()
            }
            bstack1ll1l11lll1_opy_[key].append(hook)
            bstack1ll1111ll11_opy_[bstack1l1l1l111ll_opy_.bstack1ll11l1111l_opy_] = key
        elif test_hook_state == bstack1lll1lll11l_opy_.POST:
            bstack1ll1ll11111_opy_ = bstack1ll1l11lll1_opy_.get(key, [])
            hook = bstack1ll1ll11111_opy_.pop() if bstack1ll1ll11111_opy_ else None
            if hook:
                result = self.__1ll11ll1l1l_opy_(*args)
                if result:
                    bstack1l1lllllll1_opy_ = result.get(bstack111111l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᖙ"), TestFramework.bstack1ll11ll1l11_opy_)
                    if bstack1l1lllllll1_opy_ != TestFramework.bstack1ll11ll1l11_opy_:
                        hook[TestFramework.bstack1ll11l111ll_opy_] = bstack1l1lllllll1_opy_
                hook[TestFramework.bstack1ll111ll1ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1ll1l1_opy_]= bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()
                self.bstack1ll1l11ll1l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l11l1l_opy_, [])
                if logs: self.bstack1ll11111111_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll1111ll11_opy_[bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_] = key
        TestFramework.bstack1ll1l11l111_opy_(instance, bstack1ll1111ll11_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨᖚ") + str(bstack1l1llllll11_opy_) + bstack111111l_opy_ (u"ࠣࠤᖛ"))
    def __1ll111llll1_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11111l11_opy_(args[0], [bstack111111l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᖜ"), bstack111111l_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦᖝ"), bstack111111l_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᖞ"), bstack111111l_opy_ (u"ࠧ࡯ࡤࡴࠤᖟ"), bstack111111l_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣᖠ"), bstack111111l_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢᖡ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack111111l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖢ")) else fixturedef.get(bstack111111l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᖣ"), None)
        fixturename = request.fixturename if hasattr(request, bstack111111l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᖤ")) else None
        node = request.node if hasattr(request, bstack111111l_opy_ (u"ࠦࡳࡵࡤࡦࠤᖥ")) else None
        target = request.node.nodeid if hasattr(node, bstack111111l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᖦ")) else None
        baseid = fixturedef.get(bstack111111l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨᖧ"), None) or bstack111111l_opy_ (u"ࠢࠣᖨ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack111111l_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨᖩ")):
            target = bstack1l1l1l111ll_opy_.__1ll1l111111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack111111l_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦᖪ")) else None
            if target and not TestFramework.bstack1ll11ll1lll_opy_(target):
                self.__1ll1l11111l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᖫ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠦࠧᖬ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack111111l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥᖭ") + str(target) + bstack111111l_opy_ (u"ࠨࠢᖮ"))
            return None
        instance = TestFramework.bstack1ll11ll1lll_opy_(target)
        if not instance:
            self.logger.warning(bstack111111l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤᖯ") + str(target) + bstack111111l_opy_ (u"ࠣࠤᖰ"))
            return None
        bstack1ll11l1llll_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll1l1lll1l_opy_, {})
        if os.getenv(bstack111111l_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥᖱ"), bstack111111l_opy_ (u"ࠥ࠵ࠧᖲ")) == bstack111111l_opy_ (u"ࠦ࠶ࠨᖳ"):
            bstack1ll11l11l11_opy_ = bstack111111l_opy_ (u"ࠧࡀࠢᖴ").join((scope, fixturename))
            bstack1ll1l1l1111_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1111111l_opy_ = {
                bstack111111l_opy_ (u"ࠨ࡫ࡦࡻࠥᖵ"): bstack1ll11l11l11_opy_,
                bstack111111l_opy_ (u"ࠢࡵࡣࡪࡷࠧᖶ"): bstack1l1l1l111ll_opy_.__1ll11l111l1_opy_(request.node),
                bstack111111l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤᖷ"): fixturedef,
                bstack111111l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᖸ"): scope,
                bstack111111l_opy_ (u"ࠥࡸࡾࡶࡥࠣᖹ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll11l_opy_.POST and callable(getattr(args[-1], bstack111111l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣᖺ"), None)):
                    bstack1ll1111111l_opy_[bstack111111l_opy_ (u"ࠧࡺࡹࡱࡧࠥᖻ")] = TestFramework.bstack1ll1l1ll11l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1111111l_opy_[bstack111111l_opy_ (u"ࠨࡵࡶ࡫ࡧࠦᖼ")] = uuid4().__str__()
                bstack1ll1111111l_opy_[bstack1l1l1l111ll_opy_.bstack1ll11lllll1_opy_] = bstack1ll1l1l1111_opy_
            elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1ll1111111l_opy_[bstack1l1l1l111ll_opy_.bstack1ll111ll1ll_opy_] = bstack1ll1l1l1111_opy_
            if bstack1ll11l11l11_opy_ in bstack1ll11l1llll_opy_:
                bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_].update(bstack1ll1111111l_opy_)
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣᖽ") + str(bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_]) + bstack111111l_opy_ (u"ࠣࠤᖾ"))
            else:
                bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_] = bstack1ll1111111l_opy_
                self.logger.debug(bstack111111l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧᖿ") + str(len(bstack1ll11l1llll_opy_)) + bstack111111l_opy_ (u"ࠥࠦᗀ"))
        TestFramework.bstack1llll1lll1l_opy_(instance, bstack1l1l1l111ll_opy_.bstack1ll1l1lll1l_opy_, bstack1ll11l1llll_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᗁ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠧࠨᗂ"))
        return instance
    def __1ll1l11111l_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        ob = bstack1lll1lll1l1_opy_(ctx, self.bstack1ll11l11ll1_opy_, self.bstack1ll11lll11l_opy_, test_framework_state)
        TestFramework.bstack1ll1l11l111_opy_(ob, {
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_name,
            TestFramework.bstack1llll1l11l1_opy_: context.test_framework_version,
            TestFramework.bstack1ll1ll11l11_opy_: [],
            bstack1l1l1l111ll_opy_.bstack1ll1l1lll1l_opy_: {},
            bstack1l1l1l111ll_opy_.bstack1ll111l11l1_opy_: {},
            bstack1l1l1l111ll_opy_.bstack1ll1l11ll11_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1lll1l_opy_(ob, TestFramework.bstack1ll111l1lll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1lll1l_opy_(ob, TestFramework.bstack1llllllll1l_opy_, context.platform_index)
        TestFramework.bstack1llll111l1l_opy_[ctx.id] = ob
        self.logger.debug(bstack111111l_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᗃ") + str(TestFramework.bstack1llll111l1l_opy_.keys()) + bstack111111l_opy_ (u"ࠢࠣᗄ"))
        return ob
    def bstack1l1lllll11l_opy_(self, instance: bstack1lll1lll1l1_opy_, bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll1111l111_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll11l1111l_opy_
            if bstack1lllll1l1ll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_
        )
        hook = bstack1l1l1l111ll_opy_.bstack1l1lllll111_opy_(instance, bstack1ll1111l111_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l1l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, []))
        return entries
    def bstack1l1llll1lll_opy_(self, instance: bstack1lll1lll1l1_opy_, bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll1111l111_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll11l1111l_opy_
            if bstack1lllll1l1ll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_
        )
        bstack1l1l1l111ll_opy_.bstack1ll11ll1ll1_opy_(instance, bstack1ll1111l111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, []).clear()
    def bstack1ll1l11ll1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack111111l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡳࡪ࡯࡬ࡰࡦࡸࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡣࡹࡥࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫࡭ࡸࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡉࡨࡦࡥ࡮ࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡫ࡱࡷ࡮ࡪࡥࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠲࡙ࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡈࡲࡶࠥ࡫ࡡࡤࡪࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹࠬࠡࡴࡨࡴࡱࡧࡣࡦࡵ࡙ࠣࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥࠤ࡮ࡴࠠࡪࡶࡶࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡋࡩࠤࡦࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡪࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡮ࡣࡷࡧ࡭࡫ࡳࠡࡣࠣࡱࡴࡪࡩࡧ࡫ࡨࡨࠥ࡮࡯ࡰ࡭࠰ࡰࡪࡼࡥ࡭ࠢࡩ࡭ࡱ࡫ࠬࠡ࡫ࡷࠤࡨࡸࡥࡢࡶࡨࡷࠥࡧࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡘ࡯࡭ࡪ࡮ࡤࡶࡱࡿࠬࠡ࡫ࡷࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢ࡯ࡳࡨࡧࡴࡦࡦࠣ࡭ࡳࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡤࡼࠤࡷ࡫ࡰ࡭ࡣࡦ࡭ࡳ࡭ࠠࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡕࡪࡨࠤࡨࡸࡥࡢࡶࡨࡨࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡣࡵࡩࠥࡧࡤࡥࡧࡧࠤࡹࡵࠠࡵࡪࡨࠤ࡭ࡵ࡯࡬ࠩࡶࠤࠧࡲ࡯ࡨࡵࠥࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡀࠠࡕࡪࡨࠤࡪࡼࡥ࡯ࡶࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶࠤࡦࡴࡤࠡࡪࡲࡳࡰࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡗࡩࡸࡺࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᗅ")
        global _1ll111l1ll1_opy_
        platform_index = os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᗆ")]
        bstack1ll1ll111ll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1ll1l1l1lll_opy_ + str(platform_index)), bstack11llll1ll1l_opy_)
        if not os.path.exists(bstack1ll1ll111ll_opy_) or not os.path.isdir(bstack1ll1ll111ll_opy_):
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺࡳࠡࡶࡲࠤࡵࡸ࡯ࡤࡧࡶࡷࠥࢁࡽࠣᗇ").format(bstack1ll1ll111ll_opy_))
            return
        logs = hook.get(bstack111111l_opy_ (u"ࠦࡱࡵࡧࡴࠤᗈ"), [])
        with os.scandir(bstack1ll1ll111ll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l1ll1_opy_:
                    self.logger.info(bstack111111l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᗉ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack111111l_opy_ (u"ࠨࠢᗊ")
                    log_entry = bstack1ll111lll11_opy_(
                        kind=bstack111111l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᗋ"),
                        message=bstack111111l_opy_ (u"ࠣࠤᗌ"),
                        level=bstack111111l_opy_ (u"ࠤࠥᗍ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1ll11_opy_=entry.stat().st_size,
                        bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᗎ"),
                        bstack1111l1l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l1l1ll1_opy_=hook.get(TestFramework.bstack1ll1l1111l1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l1ll1_opy_.add(abs_path)
        platform_index = os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᗏ")]
        bstack1ll11lll1l1_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1ll1l1l1lll_opy_ + str(platform_index)), bstack11llll1ll1l_opy_, bstack11llll1l11l_opy_)
        if not os.path.exists(bstack1ll11lll1l1_opy_) or not os.path.isdir(bstack1ll11lll1l1_opy_):
            self.logger.info(bstack111111l_opy_ (u"ࠧࡔ࡯ࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡨࡲࡹࡳࡪࠠࡢࡶ࠽ࠤࢀࢃࠢᗐ").format(bstack1ll11lll1l1_opy_))
        else:
            self.logger.info(bstack111111l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡧࡴࡲࡱࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠻ࠢࡾࢁࠧᗑ").format(bstack1ll11lll1l1_opy_))
            with os.scandir(bstack1ll11lll1l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l1ll1_opy_:
                        self.logger.info(bstack111111l_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧᗒ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack111111l_opy_ (u"ࠣࠤᗓ")
                        log_entry = bstack1ll111lll11_opy_(
                            kind=bstack111111l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᗔ"),
                            message=bstack111111l_opy_ (u"ࠥࠦᗕ"),
                            level=bstack111111l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᗖ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1ll11_opy_=entry.stat().st_size,
                            bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᗗ"),
                            bstack1111l1l_opy_=os.path.abspath(entry.path),
                            bstack1ll1ll111l1_opy_=hook.get(TestFramework.bstack1ll1l1111l1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l1ll1_opy_.add(abs_path)
        hook[bstack111111l_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᗘ")] = logs
    def bstack1ll11111111_opy_(
        self,
        bstack1ll11l11lll_opy_: bstack1lll1lll1l1_opy_,
        entries: List[bstack1ll111lll11_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦᗙ"))
        req.platform_index = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llllllll1l_opy_)
        req.execution_context.hash = str(bstack1ll11l11lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1l11l1_opy_)
            log_entry.uuid = entry.bstack1ll1l1l1ll1_opy_
            log_entry.test_framework_state = bstack1ll11l11lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack111111l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᗚ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack111111l_opy_ (u"ࠤࠥᗛ")
            if entry.kind == bstack111111l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᗜ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1ll11_opy_
                log_entry.file_path = entry.bstack1111l1l_opy_
        def bstack1ll1l111l11_opy_():
            bstack1111ll111_opy_ = datetime.now()
            try:
                self.bstack111111111l_opy_.LogCreatedEvent(req)
                bstack1ll11l11lll_opy_.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣᗝ"), datetime.now() - bstack1111ll111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack111111l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡽࢀࠦᗞ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l111l11_opy_)
    def __1ll111ll1l1_opy_(self, instance) -> None:
        bstack111111l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡐࡴࡧࡤࡴࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡲࡦࡣࡷࡩࡸࠦࡡࠡࡦ࡬ࡧࡹࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡢࡰࡧࠤࡺࡶࡤࡢࡶࡨࡷࠥࡺࡨࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡸࡺࡡࡵࡧࠣࡹࡸ࡯࡮ࡨࠢࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᗟ")
        bstack1ll1111ll11_opy_ = {bstack111111l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤᗠ"): bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1l11l111_opy_(instance, bstack1ll1111ll11_opy_)
    @staticmethod
    def bstack1l1lllll111_opy_(instance: bstack1lll1lll1l1_opy_, bstack1ll1111l111_opy_: str):
        bstack1ll111ll11l_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll111l11l1_opy_
            if bstack1ll1111l111_opy_ == bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_
            else bstack1l1l1l111ll_opy_.bstack1ll1l11ll11_opy_
        )
        bstack1ll111l11ll_opy_ = TestFramework.get_state(instance, bstack1ll1111l111_opy_, None)
        bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None) if bstack1ll111l11ll_opy_ else None
        return (
            bstack1ll1l111ll1_opy_[bstack1ll111l11ll_opy_][-1]
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1ll111l11ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1ll1_opy_(instance: bstack1lll1lll1l1_opy_, bstack1ll1111l111_opy_: str):
        hook = bstack1l1l1l111ll_opy_.bstack1l1lllll111_opy_(instance, bstack1ll1111l111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l1l1_opy_, []).clear()
    @staticmethod
    def __1ll1l111l1l_opy_(instance: bstack1lll1lll1l1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack111111l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡤࡱࡵࡨࡸࠨᗡ"), None)):
            return
        if os.getenv(bstack111111l_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡎࡒࡋࡘࠨᗢ"), bstack111111l_opy_ (u"ࠥ࠵ࠧᗣ")) != bstack111111l_opy_ (u"ࠦ࠶ࠨᗤ"):
            bstack1l1l1l111ll_opy_.logger.warning(bstack111111l_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵ࡭ࡳ࡭ࠠࡤࡣࡳࡰࡴ࡭ࠢᗥ"))
            return
        bstack1ll11ll11ll_opy_ = {
            bstack111111l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᗦ"): (bstack1l1l1l111ll_opy_.bstack1ll11l1111l_opy_, bstack1l1l1l111ll_opy_.bstack1ll1l11ll11_opy_),
            bstack111111l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᗧ"): (bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_, bstack1l1l1l111ll_opy_.bstack1ll111l11l1_opy_),
        }
        for when in (bstack111111l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᗨ"), bstack111111l_opy_ (u"ࠤࡦࡥࡱࡲࠢᗩ"), bstack111111l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᗪ")):
            bstack1ll11ll111l_opy_ = args[1].get_records(when)
            if not bstack1ll11ll111l_opy_:
                continue
            records = [
                bstack1ll111lll11_opy_(
                    kind=TestFramework.bstack1ll1l1l11l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack111111l_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠢᗫ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack111111l_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࠨᗬ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11ll111l_opy_
                if isinstance(getattr(r, bstack111111l_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢᗭ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11111lll_opy_, bstack1ll111ll11l_opy_ = bstack1ll11ll11ll_opy_.get(when, (None, None))
            bstack1ll1l11l1ll_opy_ = TestFramework.get_state(instance, bstack1ll11111lll_opy_, None) if bstack1ll11111lll_opy_ else None
            bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None) if bstack1ll1l11l1ll_opy_ else None
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1ll1l11l1ll_opy_, [])) > 0:
                hook = bstack1ll1l111ll1_opy_[bstack1ll1l11l1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l1l1_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l1l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l11llll_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l1l111ll_opy_.__1ll1l111111_opy_(test.location) if hasattr(test, bstack111111l_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤᗮ")) else getattr(test, bstack111111l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᗯ"), None)
        test_name = test.name if hasattr(test, bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᗰ")) else None
        bstack1l1llllll1l_opy_ = test.fspath.strpath if hasattr(test, bstack111111l_opy_ (u"ࠥࡪࡸࡶࡡࡵࡪࠥᗱ")) and test.fspath else None
        if not test_id or not test_name or not bstack1l1llllll1l_opy_:
            return None
        code = None
        if hasattr(test, bstack111111l_opy_ (u"ࠦࡴࡨࡪࠣᗲ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1l1ll_opy_ = []
        try:
            bstack11llll1l1ll_opy_ = bstack1ll1l1ll_opy_.bstack1l1ll1l1_opy_(test)
        except:
            bstack1l1l1l111ll_opy_.logger.warning(bstack111111l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡴࡦࡵࡷࠤࡸࡩ࡯ࡱࡧࡶ࠰ࠥࡺࡥࡴࡶࠣࡷࡨࡵࡰࡦࡵࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤࡷ࡫ࡳࡰ࡮ࡹࡩࡩࠦࡩ࡯ࠢࡆࡐࡎࠨᗳ"))
        return {
            TestFramework.bstack1llll11lll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11l11l_opy_: test_id,
            TestFramework.bstack1ll11lll111_opy_: test_name,
            TestFramework.bstack1ll11ll11l1_opy_: getattr(test, bstack111111l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗴ"), None),
            TestFramework.bstack1ll11111l1l_opy_: bstack1l1llllll1l_opy_,
            TestFramework.bstack1ll11lll1ll_opy_: bstack1l1l1l111ll_opy_.__1ll11l111l1_opy_(test),
            TestFramework.bstack1ll1111llll_opy_: code,
            TestFramework.bstack1lll1ll1ll1_opy_: TestFramework.bstack1ll11llll1l_opy_,
            TestFramework.bstack1lll11ll1l1_opy_: test_id,
            TestFramework.bstack1l1111l1l1l_opy_: bstack11llll1l1ll_opy_
        }
    @staticmethod
    def __1ll11l111l1_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack111111l_opy_ (u"ࠢࡰࡹࡱࡣࡲࡧࡲ࡬ࡧࡵࡷࠧᗵ"), [])
            markers.extend([getattr(m, bstack111111l_opy_ (u"ࠣࡰࡤࡱࡪࠨᗶ"), None) for m in own_markers if getattr(m, bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᗷ"), None)])
            current = getattr(current, bstack111111l_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᗸ"), None)
        return markers
    @staticmethod
    def __1ll1l111111_opy_(location):
        return bstack111111l_opy_ (u"ࠦ࠿ࡀࠢᗹ").join(filter(lambda x: isinstance(x, str), location))