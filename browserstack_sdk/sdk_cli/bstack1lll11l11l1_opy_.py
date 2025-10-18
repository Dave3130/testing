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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1lll11l1111_opy_,
    bstack1llll1l1111_opy_,
    bstack1lll1lllll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_, bstack1lll1l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1ll_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l11ll1_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111ll1l_opy_(bstack1lll1l111l1_opy_):
    bstack1lll1l1lll1_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᆀ")
    bstack1lll11lll11_opy_ = bstack11l111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᆁ")
    bstack1lll11l1lll_opy_ = bstack11l111_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᆂ")
    bstack1lll1ll1l1l_opy_ = bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᆃ")
    bstack1lll1l11l1l_opy_ = bstack11l111_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᆄ")
    bstack1llll111l1l_opy_ = bstack11l111_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᆅ")
    bstack1llll1111ll_opy_ = bstack11l111_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᆆ")
    bstack1llll111111_opy_ = bstack11l111_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᆇ")
    def __init__(self):
        super().__init__(bstack1llll11l111_opy_=self.bstack1lll1l1lll1_opy_, frameworks=[bstack1lllll11l1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.BEFORE_EACH, bstack1lll11lll1l_opy_.POST), self.bstack1lll111l111_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1llll111lll_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111l1ll_opy_ = self.bstack1lll111llll_opy_(instance.context)
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆈ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠤࠥᆉ"))
        f.bstack1llllllll1l_opy_(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, bstack1lll111l1ll_opy_)
        bstack1lll111lll1_opy_ = self.bstack1lll111llll_opy_(instance.context, bstack1lll11111l1_opy_=False)
        f.bstack1llllllll1l_opy_(instance, bstack1lll111ll1l_opy_.bstack1lll11l1lll_opy_, bstack1lll111lll1_opy_)
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111ll1l_opy_.bstack1llll1111ll_opy_, False):
            self.__1lll1111ll1_opy_(f,instance,bstack1lllll1ll11_opy_)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111ll1l_opy_.bstack1llll1111ll_opy_, False):
            self.__1lll1111ll1_opy_(f, instance, bstack1lllll1ll11_opy_)
        if not f.get_state(instance, bstack1lll111ll1l_opy_.bstack1llll111111_opy_, False):
            self.__1lll1111l1l_opy_(f, instance, bstack1lllll1ll11_opy_)
    def bstack1lll111111l_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111l11l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111ll1l_opy_.bstack1llll111111_opy_, False):
            return
        driver.execute_script(
            bstack11l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆊ").format(
                json.dumps(
                    {
                        bstack11l111_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆋ"): bstack11l111_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᆌ"),
                        bstack11l111_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆍ"): {bstack11l111_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᆎ"): result},
                    }
                )
            )
        )
        f.bstack1llllllll1l_opy_(instance, bstack1lll111ll1l_opy_.bstack1llll111111_opy_, True)
    def bstack1lll111llll_opy_(self, context: bstack1lll1lllll1_opy_, bstack1lll11111l1_opy_= True):
        if bstack1lll11111l1_opy_:
            bstack1lll111l1ll_opy_ = self.bstack1lll11ll1l1_opy_(context, reverse=True)
        else:
            bstack1lll111l1ll_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll111l1ll_opy_ if f[1].state != bstack1lllll1lll1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1ll11l11l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def __1lll1111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᆏ")).get(bstack11l111_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᆐ")):
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
            if not bstack1lll111l1ll_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᆑ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠦࠧᆒ"))
                return
            driver = bstack1lll111l1ll_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_, None)
            if not status:
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆓ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠨࠢᆔ"))
                return
            bstack1llll111l11_opy_ = {bstack11l111_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᆕ"): status.lower()}
            bstack1lll1l1llll_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
            if status.lower() == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᆖ") and bstack1lll1l1llll_opy_ is not None:
                bstack1llll111l11_opy_[bstack11l111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᆗ")] = bstack1lll1l1llll_opy_[0][bstack11l111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᆘ")][0] if isinstance(bstack1lll1l1llll_opy_, list) else str(bstack1lll1l1llll_opy_)
            driver.execute_script(
                bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆙ").format(
                    json.dumps(
                        {
                            bstack11l111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆚ"): bstack11l111_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᆛ"),
                            bstack11l111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆜ"): bstack1llll111l11_opy_,
                        }
                    )
                )
            )
            f.bstack1llllllll1l_opy_(instance, bstack1lll111ll1l_opy_.bstack1llll111111_opy_, True)
    @measure(event_name=EVENTS.bstack1l111lll1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def __1lll1111ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᆝ")).get(bstack11l111_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᆞ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11l111l_opy_, None)
            if not test_name:
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᆟ"))
                return
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
            if not bstack1lll111l1ll_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᆠ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠧࠨᆡ"))
                return
            for bstack1lll11111ll_opy_, bstack1lll1111lll_opy_ in bstack1lll111l1ll_opy_:
                if not bstack1lllll11l1l_opy_.bstack1lll111l11l_opy_(bstack1lll1111lll_opy_):
                    continue
                driver = bstack1lll11111ll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᆢ").format(
                        json.dumps(
                            {
                                bstack11l111_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆣ"): bstack11l111_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᆤ"),
                                bstack11l111_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆥ"): {bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᆦ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llllllll1l_opy_(instance, bstack1lll111ll1l_opy_.bstack1llll1111ll_opy_, True)
    def bstack1lll1ll111l_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        bstack1lll111l1ll_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])]
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᆧ"))
            return
        if not bstack1lll1l11ll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᆨ"))
            return
        for bstack1lll1111l11_opy_ in bstack1lll111l1ll_opy_:
            driver = bstack1lll1111l11_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11l111_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᆩ") + str(timestamp)
            driver.execute_script(
                bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆪ").format(
                    json.dumps(
                        {
                            bstack11l111_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆫ"): bstack11l111_opy_ (u"ࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦᆬ"),
                            bstack11l111_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆭ"): {
                                bstack11l111_opy_ (u"ࠦࡹࡿࡰࡦࠤᆮ"): bstack11l111_opy_ (u"ࠧࡇ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠤᆯ"),
                                bstack11l111_opy_ (u"ࠨࡤࡢࡶࡤࠦᆰ"): data,
                                bstack11l111_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࠨᆱ"): bstack11l111_opy_ (u"ࠣࡦࡨࡦࡺ࡭ࠢᆲ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        keys = [
            bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_,
            bstack1lll111ll1l_opy_.bstack1lll11l1lll_opy_,
        ]
        bstack1lll111l1ll_opy_ = []
        for key in keys:
            bstack1lll111l1ll_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡴࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᆳ"))
            return
        if f.get_state(instance, bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_, False):
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡈࡈࡔࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡦࡶࡪࡧࡴࡦࡦࠥᆴ"))
            return
        self.bstack1llll1lll11_opy_()
        bstack1l1ll1ll1_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        for bstack1lll11111ll_opy_, driver in bstack1lll111l1ll_opy_:
            try:
                webdriver = bstack1lll11111ll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11l111_opy_ (u"ࠦ࡜࡫ࡢࡅࡴ࡬ࡺࡪࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠣࠬࡷ࡫ࡦࡦࡴࡨࡲࡨ࡫ࠠࡦࡺࡳ࡭ࡷ࡫ࡤࠪࠤᆵ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᆶ")
                    if bstack1lllll11l1l_opy_.get_state(driver, bstack1lllll11l1l_opy_.bstack1lll11l11ll_opy_, False)
                    else bstack11l111_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᆷ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll11l1l_opy_.get_state(driver, bstack1lllll11l1l_opy_.bstack1llll111ll1_opy_, bstack11l111_opy_ (u"ࠢࠣᆸ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll11l1l_opy_.get_state(driver, bstack1lllll11l1l_opy_.bstack1lll1ll1l11_opy_, bstack11l111_opy_ (u"ࠣࠤᆹ"))
                caps = None
                if hasattr(webdriver, bstack11l111_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆺ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11l111_opy_ (u"ࠥࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆻ"))
                    except Exception as e:
                        self.logger.debug(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠯ࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠺ࠡࠤᆼ") + str(e) + bstack11l111_opy_ (u"ࠧࠨᆽ"))
                try:
                    bstack1lll111ll11_opy_ = json.dumps(caps).encode(bstack11l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆾ")) if caps else bstack1lll111l1l1_opy_ (u"ࠢࡼࡿࠥᆿ")
                    req.capabilities = bstack1lll111ll11_opy_
                except Exception as e:
                    self.logger.debug(bstack11l111_opy_ (u"ࠣࡩࡨࡸࡤࡩࡢࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡷࡪࡸࡩࡢ࡮࡬ࡾࡪࠦࡣࡢࡲࡶࠤ࡫ࡵࡲࠡࡴࡨࡵࡺ࡫ࡳࡵ࠼ࠣࠦᇀ") + str(e) + bstack11l111_opy_ (u"ࠤࠥᇁ"))
            except Exception as e:
                self.logger.error(bstack11l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡤࡳ࡫ࡹࡩࡷࠦࡩࡵࡧࡰ࠾ࠥࠨᇂ") + str(str(e)) + bstack11l111_opy_ (u"ࠦࠧᇃ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll11lllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll1l11ll1_opy_() and len(bstack1lll111l1ll_opy_) == 0:
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11l1lll_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇄ") + str(kwargs) + bstack11l111_opy_ (u"ࠨࠢᇅ"))
            return {}
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇆ") + str(kwargs) + bstack11l111_opy_ (u"ࠣࠤᇇ"))
            return {}
        bstack1lll11111ll_opy_, bstack1lll1llllll_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1lll11111ll_opy_()
        if not driver:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇈ") + str(kwargs) + bstack11l111_opy_ (u"ࠥࠦᇉ"))
            return {}
        capabilities = f.get_state(bstack1lll1llllll_opy_, bstack1lllll11l1l_opy_.bstack1lll1ll1111_opy_)
        if not capabilities:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇊ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᇋ"))
            return {}
        return capabilities.get(bstack11l111_opy_ (u"ࠨࡡ࡭ࡹࡤࡽࡸࡓࡡࡵࡥ࡫ࠦᇌ"), {})
    def bstack1lll1l1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll1l11ll1_opy_() and len(bstack1lll111l1ll_opy_) == 0:
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11l1lll_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇍ") + str(kwargs) + bstack11l111_opy_ (u"ࠣࠤᇎ"))
            return
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇏ") + str(kwargs) + bstack11l111_opy_ (u"ࠥࠦᇐ"))
        bstack1lll11111ll_opy_, bstack1lll1llllll_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1lll11111ll_opy_()
        if not driver:
            self.logger.debug(bstack11l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇑ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᇒ"))
            return
        return driver