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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_, bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll11_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll1l1_opy_, bstack1lll1lll11l_opy_, bstack1ll111lll11_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll1l1l_opy_, bstack1ll11llllll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11ll11l1l_opy_ = [bstack111111l_opy_ (u"ࠥࡲࡦࡳࡥࠣᎥ"), bstack111111l_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᎦ"), bstack111111l_opy_ (u"ࠧࡩ࡯࡯ࡨ࡬࡫ࠧᎧ"), bstack111111l_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࠢᎨ"), bstack111111l_opy_ (u"ࠢࡱࡣࡷ࡬ࠧᎩ")]
bstack1ll111l1l1l_opy_ = bstack1ll11llllll_opy_()
bstack1ll1l1l1lll_opy_ = bstack111111l_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᎪ")
bstack1l11l11111l_opy_ = {
    bstack111111l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡌࡸࡪࡳࠢᎫ"): bstack1l11ll11l1l_opy_,
    bstack111111l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡔࡦࡩ࡫ࡢࡩࡨࠦᎬ"): bstack1l11ll11l1l_opy_,
    bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡒࡵࡤࡶ࡮ࡨࠦᎭ"): bstack1l11ll11l1l_opy_,
    bstack111111l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡉ࡬ࡢࡵࡶࠦᎮ"): bstack1l11ll11l1l_opy_,
    bstack111111l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡆࡶࡰࡦࡸ࡮ࡵ࡮ࠣᎯ"): bstack1l11ll11l1l_opy_
    + [
        bstack111111l_opy_ (u"ࠢࡰࡴ࡬࡫࡮ࡴࡡ࡭ࡰࡤࡱࡪࠨᎰ"),
        bstack111111l_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᎱ"),
        bstack111111l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧ࡬ࡲ࡫ࡵࠢᎲ"),
        bstack111111l_opy_ (u"ࠥ࡯ࡪࡿࡷࡰࡴࡧࡷࠧᎳ"),
        bstack111111l_opy_ (u"ࠦࡨࡧ࡬࡭ࡵࡳࡩࡨࠨᎴ"),
        bstack111111l_opy_ (u"ࠧࡩࡡ࡭࡮ࡲࡦ࡯ࠨᎵ"),
        bstack111111l_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧᎶ"),
        bstack111111l_opy_ (u"ࠢࡴࡶࡲࡴࠧᎷ"),
        bstack111111l_opy_ (u"ࠣࡦࡸࡶࡦࡺࡩࡰࡰࠥᎸ"),
        bstack111111l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᎹ"),
    ],
    bstack111111l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦ࡯࡮࠯ࡕࡨࡷࡸ࡯࡯࡯ࠤᎺ"): [bstack111111l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡳࡥࡹ࡮ࠢᎻ"), bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡶࡪࡦ࡯࡬ࡦࡦࠥᎼ"), bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡷࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢᎽ"), bstack111111l_opy_ (u"ࠢࡪࡶࡨࡱࡸࠨᎾ")],
    bstack111111l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡥࡲࡲ࡫࡯ࡧ࠯ࡅࡲࡲ࡫࡯ࡧࠣᎿ"): [bstack111111l_opy_ (u"ࠤ࡬ࡲࡻࡵࡣࡢࡶ࡬ࡳࡳࡥࡰࡢࡴࡤࡱࡸࠨᏀ"), bstack111111l_opy_ (u"ࠥࡥࡷ࡭ࡳࠣᏁ")],
    bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡆࡪࡺࡷࡹࡷ࡫ࡄࡦࡨࠥᏂ"): [bstack111111l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᏃ"), bstack111111l_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᏄ"), bstack111111l_opy_ (u"ࠢࡧࡷࡱࡧࠧᏅ"), bstack111111l_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᏆ"), bstack111111l_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᏇ"), bstack111111l_opy_ (u"ࠥ࡭ࡩࡹࠢᏈ")],
    bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡓࡶࡤࡕࡩࡶࡻࡥࡴࡶࠥᏉ"): [bstack111111l_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥᏊ"), bstack111111l_opy_ (u"ࠨࡰࡢࡴࡤࡱࠧᏋ"), bstack111111l_opy_ (u"ࠢࡱࡣࡵࡥࡲࡥࡩ࡯ࡦࡨࡼࠧᏌ")],
    bstack111111l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡴࡸࡲࡳ࡫ࡲ࠯ࡅࡤࡰࡱࡏ࡮ࡧࡱࠥᏍ"): [bstack111111l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᏎ"), bstack111111l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࠥᏏ")],
    bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡎࡰࡦࡨࡏࡪࡿࡷࡰࡴࡧࡷࠧᏐ"): [bstack111111l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᏑ"), bstack111111l_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᏒ")],
    bstack111111l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡐࡥࡷࡱࠢᏓ"): [bstack111111l_opy_ (u"ࠣࡰࡤࡱࡪࠨᏔ"), bstack111111l_opy_ (u"ࠤࡤࡶ࡬ࡹࠢᏕ"), bstack111111l_opy_ (u"ࠥ࡯ࡼࡧࡲࡨࡵࠥᏖ")],
}
_1ll111l1ll1_opy_ = set()
class bstack1l11llllll1_opy_(bstack1llllll111l_opy_):
    bstack1l11ll11ll1_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡩ࡫࡫ࡲࡳࡧࡧࠦᏗ")
    bstack1l11ll1l1l1_opy_ = bstack111111l_opy_ (u"ࠧࡏࡎࡇࡑࠥᏘ")
    bstack1l11ll1l11l_opy_ = bstack111111l_opy_ (u"ࠨࡅࡓࡔࡒࡖࠧᏙ")
    bstack1l11l11llll_opy_: Callable
    bstack1l11ll111ll_opy_: Callable
    def __init__(self, bstack1l1l11l1lll_opy_, bstack1ll1lllll11_opy_):
        super().__init__()
        self.bstack1l11ll11lll_opy_ = bstack1ll1lllll11_opy_
        if os.getenv(bstack111111l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡏ࠲࠳࡜ࠦᏚ"), bstack111111l_opy_ (u"ࠣ࠳ࠥᏛ")) != bstack111111l_opy_ (u"ࠤ࠴ࠦᏜ") or not self.is_enabled():
            self.logger.warning(bstack111111l_opy_ (u"ࠥࠦᏝ") + str(self.__class__.__name__) + bstack111111l_opy_ (u"ࠦࠥࡪࡩࡴࡣࡥࡰࡪࡪࠢᏞ"))
            return
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1ll1lll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll11l111_opy_)
        for event in bstack1llll111lll_opy_:
            for state in bstack1lll1lll11l_opy_:
                TestFramework.bstack1111111l11_opy_((event, state), self.bstack1l11l1ll11l_opy_)
        bstack1l1l11l1lll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.POST), self.bstack1l11ll111l1_opy_)
        self.bstack1l11l11llll_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1l11ll_opy_(bstack1l11llllll1_opy_.bstack1l11ll1l1l1_opy_, self.bstack1l11l11llll_opy_)
        self.bstack1l11ll111ll_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1l11ll_opy_(bstack1l11llllll1_opy_.bstack1l11ll1l11l_opy_, self.bstack1l11ll111ll_opy_)
        self.bstack1l11l1lll11_opy_ = builtins.print
        builtins.print = self.bstack1l11ll1l111_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1ll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll1l1lll11_opy_() and instance:
            bstack1l11l1l111l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1l1ll_opy_
            if test_framework_state == bstack1llll111lll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll111lll_opy_.LOG:
                bstack1111ll111_opy_ = datetime.now()
                entries = f.bstack1l1lllll11l_opy_(instance, bstack1lllll1l1ll_opy_)
                if entries:
                    self.bstack1ll11111111_opy_(instance, entries)
                    instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࠧᏟ"), datetime.now() - bstack1111ll111_opy_)
                    f.bstack1l1llll1lll_opy_(instance, bstack1lllll1l1ll_opy_)
                instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᏠ"), datetime.now() - bstack1l11l1l111l_opy_)
                return # do not send this event with the bstack1l11l1l1l1l_opy_ bstack1l11l11ll1l_opy_
            elif (
                test_framework_state == bstack1llll111lll_opy_.TEST
                and test_hook_state == bstack1lll1lll11l_opy_.POST
                and not f.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_)
            ):
                self.logger.warning(bstack111111l_opy_ (u"ࠢࡥࡴࡲࡴࡵ࡯࡮ࡨࠢࡧࡹࡪࠦࡴࡰࠢ࡯ࡥࡨࡱࠠࡰࡨࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࠧᏡ") + str(TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_)) + bstack111111l_opy_ (u"ࠣࠤᏢ"))
                f.bstack1llll1lll1l_opy_(instance, bstack1l11llllll1_opy_.bstack1l11ll11ll1_opy_, True)
                return # do not send this event bstack1l11l1ll111_opy_ bstack1l11l11l111_opy_
            elif (
                f.get_state(instance, bstack1l11llllll1_opy_.bstack1l11ll11ll1_opy_, False)
                and test_framework_state == bstack1llll111lll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1lll11l_opy_.POST
                and f.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_)
            ):
                self.logger.warning(bstack111111l_opy_ (u"ࠤ࡬ࡲ࡯࡫ࡣࡵ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡘࡊ࡙ࡔ࠭ࠢࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡓࡓࡘ࡚ࠠࠣᏣ") + str(TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_)) + bstack111111l_opy_ (u"ࠥࠦᏤ"))
                self.bstack1l11l1ll11l_opy_(f, instance, (bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), *args, **kwargs)
            bstack1111ll111_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l111llllll_opy_ = sorted(
                filter(lambda x: x.get(bstack111111l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᏥ"), None), data.pop(bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᏦ"), {}).values()),
                key=lambda x: x[bstack111111l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᏧ")],
            )
            if bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_ in data:
                data.pop(bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_)
            data.update({bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᏨ"): bstack1l111llllll_opy_})
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠣ࡬ࡶࡳࡳࡀࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᏩ"), datetime.now() - bstack1111ll111_opy_)
            bstack1111ll111_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11ll1111l_opy_)
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᏪ"), datetime.now() - bstack1111ll111_opy_)
            self.bstack1l11l11ll1l_opy_(instance, bstack1lllll1l1ll_opy_, event_json=event_json)
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᏫ"), datetime.now() - bstack1l11l1l111l_opy_)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
        bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack1ll1llll11_opy_.value)
        self.bstack1l11ll11lll_opy_.bstack1llll111ll1_opy_(instance, f, bstack1lllll1l1ll_opy_, *args, **kwargs)
        bstack1llllll1lll_opy_.end(EVENTS.bstack1ll1llll11_opy_.value, bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᏬ"), bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᏭ"), status=True, failure=None, test_name=None)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11ll11lll_opy_.bstack1lll1llll11_opy_(instance, f, bstack1lllll1l1ll_opy_, *args, **kwargs)
        self.bstack1l11ll11l11_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1l1111_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l11ll11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack111111l_opy_ (u"ࠨࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡖࡨࡷࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡋࡶࡦࡰࡷࠤ࡬ࡘࡐࡄࠢࡦࡥࡱࡲ࠺ࠡࡐࡲࠤࡻࡧ࡬ࡪࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡩࡧࡴࡢࠤᏮ"))
            return
        bstack1111ll111_opy_ = datetime.now()
        try:
            r = self.bstack111111111l_opy_.TestSessionEvent(req)
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡨࡺࡪࡴࡴࠣᏯ"), datetime.now() - bstack1111ll111_opy_)
            f.bstack1llll1lll1l_opy_(instance, self.bstack1l11ll11lll_opy_.bstack1llll11111l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack111111l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᏰ") + str(r) + bstack111111l_opy_ (u"ࠤࠥᏱ"))
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᏲ") + str(e) + bstack111111l_opy_ (u"ࠦࠧᏳ"))
            traceback.print_exc()
            raise e
    def bstack1l11ll111l1_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        _driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        _1l11l1lllll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llllll11ll_opy_.bstack1l1lll111l1_opy_(method_name):
            return
        if f.bstack1l1llll11l1_opy_(*args) == bstack1llllll11ll_opy_.bstack1l11l111111_opy_:
            bstack1l11l1l111l_opy_ = datetime.now()
            screenshot = result.get(bstack111111l_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᏴ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack111111l_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤ࡮ࡳࡡࡨࡧࠣࡦࡦࡹࡥ࠷࠶ࠣࡷࡹࡸࠢᏵ"))
                return
            bstack1ll11l11lll_opy_ = self.bstack1l11l1ll1ll_opy_(instance)
            if bstack1ll11l11lll_opy_:
                entry = bstack1ll111lll11_opy_(TestFramework.bstack1l11l1l1ll1_opy_, screenshot)
                self.bstack1ll11111111_opy_(bstack1ll11l11lll_opy_, [entry])
                instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡦࡺࡨࡧࡺࡺࡥࠣ᏶"), datetime.now() - bstack1l11l1l111l_opy_)
            else:
                self.logger.warning(bstack111111l_opy_ (u"ࠣࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡧࡶࡸࠥ࡬࡯ࡳࠢࡺ࡬࡮ࡩࡨࠡࡶ࡫࡭ࡸࠦࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠣࡻࡦࡹࠠࡵࡣ࡮ࡩࡳࠦࡢࡺࠢࡧࡶ࡮ࡼࡥࡳ࠿ࠣࡿࢂࠨ᏷").format(instance.ref()))
        event = {}
        bstack1ll11l11lll_opy_ = self.bstack1l11l1ll1ll_opy_(instance)
        if bstack1ll11l11lll_opy_:
            self.bstack1l11l111lll_opy_(event, bstack1ll11l11lll_opy_)
            if event.get(bstack111111l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᏸ")):
                self.bstack1ll11111111_opy_(bstack1ll11l11lll_opy_, event[bstack111111l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᏹ")])
            else:
                self.logger.debug(bstack111111l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡰࡴ࡭ࡳࠡࡨࡲࡶࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡨࡺࡪࡴࡴࠣᏺ"))
    @measure(event_name=EVENTS.bstack1l11l1l1l11_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1ll11111111_opy_(
        self,
        bstack1ll11l11lll_opy_: bstack1lll1lll1l1_opy_,
        entries: List[bstack1ll111lll11_opy_],
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llllllll1l_opy_)
        req.execution_context.hash = str(bstack1ll11l11lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1l11l1_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll11lll1_opy_)
            log_entry.test_framework_state = bstack1ll11l11lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack111111l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᏻ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack111111l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᏼ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1ll11_opy_
                log_entry.file_path = entry.bstack1111l1l_opy_
        def bstack1ll1l111l11_opy_():
            bstack1111ll111_opy_ = datetime.now()
            try:
                self.bstack111111111l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1l1ll1_opy_:
                    bstack1ll11l11lll_opy_.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᏽ"), datetime.now() - bstack1111ll111_opy_)
                elif entry.kind == TestFramework.bstack1l11l11l1l1_opy_:
                    bstack1ll11l11lll_opy_.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧ᏾"), datetime.now() - bstack1111ll111_opy_)
                else:
                    bstack1ll11l11lll_opy_.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡ࡯ࡳ࡬ࠨ᏿"), datetime.now() - bstack1111ll111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack111111l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ᐀") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l111l11_opy_)
    @measure(event_name=EVENTS.bstack1l11l111l11_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l11l11ll1l_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        event_json=None,
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll1l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l11l1_opy_)
        req.test_framework_state = bstack1lllll1l1ll_opy_[0].name
        req.test_hook_state = bstack1lllll1l1ll_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll111l1l11_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11ll1111l_opy_)).encode(bstack111111l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᐁ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll1l111l11_opy_():
            bstack1111ll111_opy_ = datetime.now()
            try:
                self.bstack111111111l_opy_.TestFrameworkEvent(req)
                instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡨࡺࡪࡴࡴࠣᐂ"), datetime.now() - bstack1111ll111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack111111l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᐃ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l111l11_opy_)
    def bstack1l11l1ll1ll_opy_(self, instance: bstack1lllll11l1l_opy_):
        bstack1l11l1l1lll_opy_ = TestFramework.bstack1l11l1111l1_opy_(instance.context)
        for t in bstack1l11l1l1lll_opy_:
            bstack1lll11l1111_opy_ = TestFramework.get_state(t, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1111_opy_):
                return t
    def bstack1l11l1111ll_opy_(self, message):
        self.bstack1l11l11llll_opy_(message + bstack111111l_opy_ (u"ࠢ࡝ࡰࠥᐄ"))
    def log_error(self, message):
        self.bstack1l11ll111ll_opy_(message + bstack111111l_opy_ (u"ࠣ࡞ࡱࠦᐅ"))
    def bstack1l11l1l11ll_opy_(self, level, original_func):
        def bstack1l11l111ll1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack111111l_opy_ (u"ࠤࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࠥᐆ") in message or bstack111111l_opy_ (u"ࠥ࡟ࡘࡊࡋࡄࡎࡌࡡࠧᐇ") in message or bstack111111l_opy_ (u"ࠦࡠ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠣᐈ") in message:
                return return_value
            bstack1l11l1l1lll_opy_ = TestFramework.bstack1l11l11l1ll_opy_()
            if not bstack1l11l1l1lll_opy_:
                return return_value
            bstack1ll11l11lll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1l1lll_opy_
                    if TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1llll11lll1_opy_)
                ),
                None,
            )
            if not bstack1ll11l11lll_opy_:
                return return_value
            entry = bstack1ll111lll11_opy_(TestFramework.bstack1ll1l1l11l1_opy_, message, level)
            self.bstack1ll11111111_opy_(bstack1ll11l11lll_opy_, [entry])
            return return_value
        return bstack1l11l111ll1_opy_
    def bstack1l11ll1l111_opy_(self):
        def bstack1l11ll11111_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1lll11_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack111111l_opy_ (u"ࠬࠦࠧᐉ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack111111l_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢᐊ") in message:
                    return
                bstack1l11l1l1lll_opy_ = TestFramework.bstack1l11l11l1ll_opy_()
                if not bstack1l11l1l1lll_opy_:
                    return
                bstack1ll11l11lll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1l1lll_opy_
                        if TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1llll11lll1_opy_)
                    ),
                    None,
                )
                if not bstack1ll11l11lll_opy_:
                    return
                entry = bstack1ll111lll11_opy_(TestFramework.bstack1ll1l1l11l1_opy_, message, bstack1l11llllll1_opy_.bstack1l11ll1l1l1_opy_)
                self.bstack1ll11111111_opy_(bstack1ll11l11lll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1lll11_opy_(bstack1llll1ll1_opy_ (u"ࠢ࡜ࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦ࡟ࠣࡐࡴ࡭ࠠࡤࡣࡳࡸࡺࡸࡥࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࡨࢁࠧᐋ"))
                except:
                    pass
        return bstack1l11ll11111_opy_
    def bstack1l11l111lll_opy_(self, event: dict, instance=None) -> None:
        global _1ll111l1ll1_opy_
        levels = [bstack111111l_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᐌ"), bstack111111l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᐍ")]
        bstack1l11ll1l1ll_opy_ = bstack111111l_opy_ (u"ࠥࠦᐎ")
        if instance is not None:
            try:
                bstack1l11ll1l1ll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
            except Exception as e:
                self.logger.warning(bstack111111l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡻࡩࡥࠢࡩࡶࡴࡳࠠࡪࡰࡶࡸࡦࡴࡣࡦࠤᐏ").format(e))
        bstack1l11l1lll1l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᐐ")]
                bstack1ll1ll111ll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1ll1l1l1lll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1ll111ll_opy_):
                    self.logger.debug(bstack111111l_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡱࡳࡹࠦࡰࡳࡧࡶࡩࡳࡺࠠࡧࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡖࡨࡷࡹࠦࡡ࡯ࡦࠣࡆࡺ࡯࡬ࡥࠢ࡯ࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᐑ").format(bstack1ll1ll111ll_opy_))
                    continue
                file_names = os.listdir(bstack1ll1ll111ll_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1ll111ll_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll111l1ll1_opy_:
                        self.logger.info(bstack111111l_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧᐒ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11l11l_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11l11l_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack111111l_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᐓ"):
                                entry = bstack1ll111lll11_opy_(
                                    kind=bstack111111l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᐔ"),
                                    message=bstack111111l_opy_ (u"ࠥࠦᐕ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l1ll11_opy_=file_size,
                                    bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᐖ"),
                                    bstack1111l1l_opy_=os.path.abspath(file_path),
                                    bstack11lll1l1ll_opy_=bstack1l11ll1l1ll_opy_
                                )
                            elif level == bstack111111l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᐗ"):
                                entry = bstack1ll111lll11_opy_(
                                    kind=bstack111111l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᐘ"),
                                    message=bstack111111l_opy_ (u"ࠢࠣᐙ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l1ll11_opy_=file_size,
                                    bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᐚ"),
                                    bstack1111l1l_opy_=os.path.abspath(file_path),
                                    bstack1ll1ll111l1_opy_=bstack1l11ll1l1ll_opy_
                                )
                            bstack1l11l1lll1l_opy_.append(entry)
                            _1ll111l1ll1_opy_.add(abs_path)
                        except Exception as bstack1l11l1ll1l1_opy_:
                            self.logger.error(bstack111111l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡨࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᐛ").format(bstack1l11l1ll1l1_opy_))
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᐜ").format(e))
        event[bstack111111l_opy_ (u"ࠦࡱࡵࡧࡴࠤᐝ")] = bstack1l11l1lll1l_opy_
class bstack1l11ll1111l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1llll1_opy_ = set()
        kwargs[bstack111111l_opy_ (u"ࠧࡹ࡫ࡪࡲ࡮ࡩࡾࡹࠢᐞ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l11lll1_opy_(obj, self.bstack1l11l1llll1_opy_)
def bstack1l11l11ll11_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l11lll1_opy_(obj, bstack1l11l1llll1_opy_=None, max_depth=3):
    if bstack1l11l1llll1_opy_ is None:
        bstack1l11l1llll1_opy_ = set()
    if id(obj) in bstack1l11l1llll1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1llll1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l1l11l1_opy_ = TestFramework.bstack1ll1l1ll11l_opy_(obj)
    bstack1l11l111l1l_opy_ = next((k.lower() in bstack1l11l1l11l1_opy_.lower() for k in bstack1l11l11111l_opy_.keys()), None)
    if bstack1l11l111l1l_opy_:
        obj = TestFramework.bstack1ll11111l11_opy_(obj, bstack1l11l11111l_opy_[bstack1l11l111l1l_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack111111l_opy_ (u"ࠨ࡟ࡠࡵ࡯ࡳࡹࡹ࡟ࡠࠤᐟ")):
            keys = getattr(obj, bstack111111l_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᐠ"), [])
        elif hasattr(obj, bstack111111l_opy_ (u"ࠣࡡࡢࡨ࡮ࡩࡴࡠࡡࠥᐡ")):
            keys = getattr(obj, bstack111111l_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᐢ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack111111l_opy_ (u"ࠥࡣࠧᐣ"))}
        if not obj and bstack1l11l1l11l1_opy_ == bstack111111l_opy_ (u"ࠦࡵࡧࡴࡩ࡮࡬ࡦ࠳ࡖ࡯ࡴ࡫ࡻࡔࡦࡺࡨࠣᐤ"):
            obj = {bstack111111l_opy_ (u"ࠧࡶࡡࡵࡪࠥᐥ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11ll11_opy_(key) or str(key).startswith(bstack111111l_opy_ (u"ࠨ࡟ࠣᐦ")):
            continue
        if value is not None and bstack1l11l11ll11_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l11lll1_opy_(value, bstack1l11l1llll1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l11lll1_opy_(o, bstack1l11l1llll1_opy_, max_depth) for o in value]))
    return result or None