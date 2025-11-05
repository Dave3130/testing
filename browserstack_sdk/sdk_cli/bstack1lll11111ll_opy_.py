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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1lll1111l11_opy_,
    bstack1llll111l1l_opy_,
    bstack1lll1lll1ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_, bstack1lll1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l11111_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11lll11_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11111l1_opy_(bstack1lll1l11111_opy_):
    bstack1lll11l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥᆒ")
    bstack1lll1l1llll_opy_ = bstack11ll1ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᆓ")
    bstack1lll1l11lll_opy_ = bstack11ll1ll_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᆔ")
    bstack1lll1l11l11_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᆕ")
    bstack1lll1ll1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧᆖ")
    bstack1llll11111l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣᆗ")
    bstack1lll11lllll_opy_ = bstack11ll1ll_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᆘ")
    bstack1lll1lllll1_opy_ = bstack11ll1ll_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤᆙ")
    def __init__(self):
        super().__init__(bstack1lll1l1l1l1_opy_=self.bstack1lll11l1l1l_opy_, frameworks=[bstack1llll1ll111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.BEFORE_EACH, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll111ll1l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1ll111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1111111_opy_ = self.bstack1lll111111l_opy_(instance.context)
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆚ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠨࠢᆛ"))
        f.bstack1lllllll1l1_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, bstack1lll1111111_opy_)
        bstack1lll111l111_opy_ = self.bstack1lll111111l_opy_(instance.context, bstack1lll1111ll1_opy_=False)
        f.bstack1lllllll1l1_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1l11lll_opy_, bstack1lll111l111_opy_)
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, False):
            self.__1ll1llllll1_opy_(f,instance,bstack1lllllllll1_opy_)
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, False):
            self.__1ll1llllll1_opy_(f, instance, bstack1lllllllll1_opy_)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1lllll1_opy_, False):
            self.__1ll1lllllll_opy_(f, instance, bstack1lllllllll1_opy_)
    def bstack1lll111l11l_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll1111l1l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1lllll1_opy_, False):
            return
        driver.execute_script(
            bstack11ll1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆜ").format(
                json.dumps(
                    {
                        bstack11ll1ll_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆝ"): bstack11ll1ll_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᆞ"),
                        bstack11ll1ll_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆟ"): {bstack11ll1ll_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᆠ"): result},
                    }
                )
            )
        )
        f.bstack1lllllll1l1_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1lllll1_opy_, True)
    def bstack1lll111111l_opy_(self, context: bstack1lll1lll1ll_opy_, bstack1lll1111ll1_opy_= True):
        if bstack1lll1111ll1_opy_:
            bstack1lll1111111_opy_ = self.bstack1lll1l11ll1_opy_(context, reverse=True)
        else:
            bstack1lll1111111_opy_ = self.bstack1lll11ll11l_opy_(context, reverse=True)
        return [f for f in bstack1lll1111111_opy_ if f[1].state != bstack1llll1l1ll1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11l1l1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1ll1lllllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᆡ")).get(bstack11ll1ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆢ")):
            bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
            if not bstack1lll1111111_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᆣ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠣࠤᆤ"))
                return
            driver = bstack1lll1111111_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_, None)
            if not status:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆥ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠥࠦᆦ"))
                return
            bstack1lll11ll111_opy_ = {bstack11ll1ll_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᆧ"): status.lower()}
            bstack1lll11l1lll_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
            if status.lower() == bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᆨ") and bstack1lll11l1lll_opy_ is not None:
                bstack1lll11ll111_opy_[bstack11ll1ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᆩ")] = bstack1lll11l1lll_opy_[0][bstack11ll1ll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᆪ")][0] if isinstance(bstack1lll11l1lll_opy_, list) else str(bstack1lll11l1lll_opy_)
            driver.execute_script(
                bstack11ll1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆫ").format(
                    json.dumps(
                        {
                            bstack11ll1ll_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆬ"): bstack11ll1ll_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᆭ"),
                            bstack11ll1ll_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆮ"): bstack1lll11ll111_opy_,
                        }
                    )
                )
            )
            f.bstack1lllllll1l1_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1lllll1_opy_, True)
    @measure(event_name=EVENTS.bstack11ll11l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def __1ll1llllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᆯ")).get(bstack11ll1ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᆰ")):
            test_name = f.get_state(instance, TestFramework.bstack1ll1lllll11_opy_, None)
            if not test_name:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᆱ"))
                return
            bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
            if not bstack1lll1111111_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᆲ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠤࠥᆳ"))
                return
            for bstack1lll1111lll_opy_, bstack1lll111l1l1_opy_ in bstack1lll1111111_opy_:
                if not bstack1llll1ll111_opy_.bstack1lll1111l1l_opy_(bstack1lll111l1l1_opy_):
                    continue
                driver = bstack1lll1111lll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11ll1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆴ").format(
                        json.dumps(
                            {
                                bstack11ll1ll_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆵ"): bstack11ll1ll_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᆶ"),
                                bstack11ll1ll_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆷ"): {bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᆸ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllllll1l1_opy_(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, True)
    def bstack1lll1l111ll_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        bstack1lll1111111_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])]
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡵࡱࠣࡰ࡮ࡴ࡫ࠣᆹ"))
            return
        if not bstack1lll11lll11_opy_():
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᆺ"))
            return
        for bstack1lll111l1ll_opy_ in bstack1lll1111111_opy_:
            driver = bstack1lll111l1ll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11ll1ll_opy_ (u"ࠥࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡖࡽࡳࡩ࠺ࠣᆻ") + str(timestamp)
            driver.execute_script(
                bstack11ll1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆼ").format(
                    json.dumps(
                        {
                            bstack11ll1ll_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆽ"): bstack11ll1ll_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣᆾ"),
                            bstack11ll1ll_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆿ"): {
                                bstack11ll1ll_opy_ (u"ࠣࡶࡼࡴࡪࠨᇀ"): bstack11ll1ll_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨᇁ"),
                                bstack11ll1ll_opy_ (u"ࠥࡨࡦࡺࡡࠣᇂ"): data,
                                bstack11ll1ll_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥᇃ"): bstack11ll1ll_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦᇄ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1l1l111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        keys = [
            bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_,
            bstack1lll11111l1_opy_.bstack1lll1l11lll_opy_,
        ]
        bstack1lll1111111_opy_ = []
        for key in keys:
            bstack1lll1111111_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡱࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡵࡱࠣࡰ࡮ࡴ࡫ࠣᇅ"))
            return
        if f.get_state(instance, bstack1lll11111l1_opy_.bstack1llll11111l_opy_, False):
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡅࡅࡘࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡣࡳࡧࡤࡸࡪࡪࠢᇆ"))
            return
        self.bstack1llllll1ll1_opy_()
        bstack111111ll11_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l11ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll1ll_opy_)
        req.test_framework_state = bstack1lllllllll1_opy_[0].name
        req.test_hook_state = bstack1lllllllll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11llll1_opy_)
        for bstack1lll1111lll_opy_, driver in bstack1lll1111111_opy_:
            try:
                webdriver = bstack1lll1111lll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11ll1ll_opy_ (u"࡙ࠣࡨࡦࡉࡸࡩࡷࡧࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠠࠩࡴࡨࡪࡪࡸࡥ࡯ࡥࡨࠤࡪࡾࡰࡪࡴࡨࡨ࠮ࠨᇇ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11ll1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣᇈ")
                    if bstack1llll1ll111_opy_.get_state(driver, bstack1llll1ll111_opy_.bstack1ll1lllll1l_opy_, False)
                    else bstack11ll1ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤᇉ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llll1ll111_opy_.get_state(driver, bstack1llll1ll111_opy_.bstack1lll11lll1l_opy_, bstack11ll1ll_opy_ (u"ࠦࠧᇊ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llll1ll111_opy_.get_state(driver, bstack1llll1ll111_opy_.bstack1lll11l1ll1_opy_, bstack11ll1ll_opy_ (u"ࠧࠨᇋ"))
                caps = None
                if hasattr(webdriver, bstack11ll1ll_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᇌ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡦ࡬ࡶࡪࡩࡴ࡭ࡻࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠯ࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᇍ"))
                    except Exception as e:
                        self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠥࠨᇎ") + str(e) + bstack11ll1ll_opy_ (u"ࠤࠥᇏ"))
                try:
                    bstack1lll111ll11_opy_ = json.dumps(caps).encode(bstack11ll1ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇐ")) if caps else bstack1lll111lll1_opy_ (u"ࠦࢀࢃࠢᇑ")
                    req.capabilities = bstack1lll111ll11_opy_
                except Exception as e:
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡦࡦࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡳࡪࠠࡴࡧࡵ࡭ࡦࡲࡩࡻࡧࠣࡧࡦࡶࡳࠡࡨࡲࡶࠥࡸࡥࡲࡷࡨࡷࡹࡀࠠࠣᇒ") + str(e) + bstack11ll1ll_opy_ (u"ࠨࠢᇓ"))
            except Exception as e:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡹ࡫࡭࠻ࠢࠥᇔ") + str(str(e)) + bstack11ll1ll_opy_ (u"ࠣࠤᇕ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll11lll11_opy_() and len(bstack1lll1111111_opy_) == 0:
            bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇖ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠥࠦᇗ"))
            return {}
        if len(bstack1lll1111111_opy_) > 1:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇘ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠧࠨᇙ"))
            return {}
        bstack1lll1111lll_opy_, bstack1llll111l11_opy_ = bstack1lll1111111_opy_[0]
        driver = bstack1lll1111lll_opy_()
        if not driver:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇚ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠢࠣᇛ"))
            return {}
        capabilities = f.get_state(bstack1llll111l11_opy_, bstack1llll1ll111_opy_.bstack1lll11ll1l1_opy_)
        if not capabilities:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇜ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᇝ"))
            return {}
        return capabilities.get(bstack11ll1ll_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣᇞ"), {})
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll11lll11_opy_() and len(bstack1lll1111111_opy_) == 0:
            bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇟ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠧࠨᇠ"))
            return
        if len(bstack1lll1111111_opy_) > 1:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇡ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠢࠣᇢ"))
        bstack1lll1111lll_opy_, bstack1llll111l11_opy_ = bstack1lll1111111_opy_[0]
        driver = bstack1lll1111lll_opy_()
        if not driver:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇣ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᇤ"))
            return
        return driver