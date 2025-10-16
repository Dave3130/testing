# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1llllll11ll_opy_,
    bstack1lll1l11l11_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack1llllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_, bstack1llll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1lll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lllll1_opy_ import bstack1llll111ll1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l111lll11_opy_ import bstack1lll11111_opy_, bstack11lll11ll1_opy_, bstack1l1ll1l111_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1llll11ll11_opy_(bstack1llll111ll1_opy_):
    bstack1lll1l1l1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᄃ")
    bstack1llll11llll_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄄ")
    bstack1lll1llll11_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄅ")
    bstack1lll1l1llll_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄆ")
    bstack1llll1l111l_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᄇ")
    bstack1llll11l111_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᄈ")
    bstack1llll11lll1_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᄉ")
    bstack1lll1lll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᄊ")
    def __init__(self):
        super().__init__(bstack1lll1l111l1_opy_=self.bstack1lll1l1l1ll_opy_, frameworks=[bstack111111111l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.BEFORE_EACH, bstack1llll1l11l1_opy_.POST), self.bstack1llll1111ll_opy_)
        if bstack1llllll1l1_opy_():
            TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l11_opy_)
        else:
            TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll11l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1llllll_opy_ = self.bstack1lll1llll1l_opy_(instance.context)
        if not bstack1lll1llllll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄋ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠥࠦᄌ"))
            return
        f.bstack1lllll1l1ll_opy_(instance, bstack1llll11ll11_opy_.bstack1llll11llll_opy_, bstack1lll1llllll_opy_)
    def bstack1lll1llll1l_opy_(self, context: bstack1lll1l11l11_opy_, bstack1lll1l1l111_opy_= True):
        if bstack1lll1l1l111_opy_:
            bstack1lll1llllll_opy_ = self.bstack1lll1l1l11l_opy_(context, reverse=True)
        else:
            bstack1lll1llllll_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll1llllll_opy_ if f[1].state != bstack11111111ll_opy_.QUIT]
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄍ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠧࠨᄎ"))
            return
        bstack1lll1llllll_opy_ = f.get_state(instance, bstack1llll11ll11_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1llllll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄏ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᄐ"))
            return
        if len(bstack1lll1llllll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄑ"))
        bstack1llll11l11l_opy_, bstack1lll1ll11l1_opy_ = bstack1lll1llllll_opy_[0]
        page = bstack1llll11l11l_opy_()
        if not page:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄒ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠥࠦᄓ"))
            return
        bstack1l1lllll11_opy_ = getattr(args[0], bstack1ll1ll1_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᄔ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᄕ")).get(bstack1ll1ll1_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᄖ")):
            try:
                page.evaluate(bstack1ll1ll1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄗ"),
                            bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬᄘ") + json.dumps(
                                bstack1l1lllll11_opy_) + bstack1ll1ll1_opy_ (u"ࠤࢀࢁࠧᄙ"))
            except Exception as e:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽࠣᄚ"), e)
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄛ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠧࠨᄜ"))
            return
        bstack1lll1llllll_opy_ = f.get_state(instance, bstack1llll11ll11_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1llllll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄝ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᄞ"))
            return
        if len(bstack1lll1llllll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄟ"))
        bstack1llll11l11l_opy_, bstack1lll1ll11l1_opy_ = bstack1lll1llllll_opy_[0]
        page = bstack1llll11l11l_opy_()
        if not page:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄠ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠥࠦᄡ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_, None)
        if not status:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄢ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠧࠨᄣ"))
            return
        bstack1llll111l1l_opy_ = {bstack1ll1ll1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᄤ"): status.lower()}
        bstack1llll1111l1_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1111_opy_, None)
        if status.lower() == bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᄥ") and bstack1llll1111l1_opy_ is not None:
            bstack1llll111l1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᄦ")] = bstack1llll1111l1_opy_[0][bstack1ll1ll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᄧ")][0] if isinstance(bstack1llll1111l1_opy_, list) else str(bstack1llll1111l1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᄨ")).get(bstack1ll1ll1_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᄩ")):
            try:
                page.evaluate(
                        bstack1ll1ll1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄪ"),
                        bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࠫᄫ")
                        + json.dumps(bstack1llll111l1l_opy_)
                        + bstack1ll1ll1_opy_ (u"ࠢࡾࠤᄬ")
                    )
            except Exception as e:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣᄭ"), e)
    def bstack1lll1ll1l1l_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(
                bstack1lll1ll111l_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄮ"))
            return
        bstack1lll1llllll_opy_ = f.get_state(instance, bstack1llll11ll11_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1llllll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄯ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠦࠧᄰ"))
            return
        if len(bstack1lll1llllll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll111l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᄱ"))
        bstack1llll11l11l_opy_, bstack1lll1ll11l1_opy_ = bstack1lll1llllll_opy_[0]
        page = bstack1llll11l11l_opy_()
        if not page:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄲ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᄳ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1ll1ll1_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᄴ") + str(timestamp)
        try:
            page.evaluate(
                bstack1ll1ll1_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᄵ"),
                bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᄶ").format(
                    json.dumps(
                        {
                            bstack1ll1ll1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᄷ"): bstack1ll1ll1_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᄸ"),
                            bstack1ll1ll1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᄹ"): {
                                bstack1ll1ll1_opy_ (u"ࠢࡵࡻࡳࡩࠧᄺ"): bstack1ll1ll1_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᄻ"),
                                bstack1ll1ll1_opy_ (u"ࠤࡧࡥࡹࡧࠢᄼ"): data,
                                bstack1ll1ll1_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᄽ"): bstack1ll1ll1_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᄾ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡱ࠴࠵ࡾࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࢀࢃࠢᄿ"), e)
    def bstack1llll1l1l11_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1llll11ll11_opy_.bstack1llll11l111_opy_, False):
            return
        self.bstack1llllll111l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1111111ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll111111_opy_)
        req.test_framework_state = bstack1llll1l1lll_opy_[0].name
        req.test_hook_state = bstack1llll1l1lll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l1l1_opy_)
        for bstack1llll11l1l1_opy_ in bstack1lll1lll1l1_opy_.bstack1lll1l1ll1l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᅀ")
                if bstack1lll1ll1lll_opy_
                else bstack1ll1ll1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᅁ")
            )
            session.ref = bstack1llll11l1l1_opy_.ref()
            session.hub_url = bstack1lll1lll1l1_opy_.get_state(bstack1llll11l1l1_opy_, bstack1lll1lll1l1_opy_.bstack1llll11ll1l_opy_, bstack1ll1ll1_opy_ (u"ࠣࠤᅂ"))
            session.framework_name = bstack1llll11l1l1_opy_.framework_name
            session.framework_version = bstack1llll11l1l1_opy_.framework_version
            session.framework_session_id = bstack1lll1lll1l1_opy_.get_state(bstack1llll11l1l1_opy_, bstack1lll1lll1l1_opy_.bstack1lll1l11l1l_opy_, bstack1ll1ll1_opy_ (u"ࠤࠥᅃ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1llllll_opy_ = f.get_state(instance, bstack1llll11ll11_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1llllll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅄ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠦࠧᅅ"))
            return
        if len(bstack1lll1llllll_opy_) > 1:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅆ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠨࠢᅇ"))
        bstack1llll11l11l_opy_, bstack1lll1ll11l1_opy_ = bstack1lll1llllll_opy_[0]
        page = bstack1llll11l11l_opy_()
        if not page:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅈ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠣࠤᅉ"))
            return
        return page
    def bstack1lll1l1ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll1ll1l11_opy_ = {}
        for bstack1llll11l1l1_opy_ in bstack1lll1lll1l1_opy_.bstack1lll1l1ll1l_opy_.values():
            caps = bstack1lll1lll1l1_opy_.get_state(bstack1llll11l1l1_opy_, bstack1lll1lll1l1_opy_.bstack1llll111lll_opy_, bstack1ll1ll1_opy_ (u"ࠤࠥᅊ"))
        bstack1lll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣᅋ")] = caps.get(bstack1ll1ll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧᅌ"), bstack1ll1ll1_opy_ (u"ࠧࠨᅍ"))
        bstack1lll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᅎ")] = caps.get(bstack1ll1ll1_opy_ (u"ࠢࡰࡵࠥᅏ"), bstack1ll1ll1_opy_ (u"ࠣࠤᅐ"))
        bstack1lll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᅑ")] = caps.get(bstack1ll1ll1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅒ"), bstack1ll1ll1_opy_ (u"ࠦࠧᅓ"))
        bstack1lll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨᅔ")] = caps.get(bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅕ"), bstack1ll1ll1_opy_ (u"ࠢࠣᅖ"))
        return bstack1lll1ll1l11_opy_
    def bstack1lll1lll111_opy_(self, page: object, bstack1llll1l11ll_opy_, args={}):
        try:
            bstack1lll1l1lll1_opy_ = bstack1ll1ll1_opy_ (u"ࠣࠤࠥࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨ࠯࠰࠱ࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠬࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡱࡩࡼࠦࡐࡳࡱࡰ࡭ࡸ࡫ࠨࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴ࠰ࡳࡹࡸ࡮ࠨࡳࡧࡶࡳࡱࡼࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡾࡪࡳࡥࡢࡰࡦࡼࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯ࠨࡼࡣࡵ࡫ࡤࡰࡳࡰࡰࢀ࠭ࠧࠨࠢᅗ")
            bstack1llll1l11ll_opy_ = bstack1llll1l11ll_opy_.replace(bstack1ll1ll1_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅘ"), bstack1ll1ll1_opy_ (u"ࠥࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠥᅙ"))
            script = bstack1lll1l1lll1_opy_.format(fn_body=bstack1llll1l11ll_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠦࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡊࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴ࠭ࠢࠥᅚ") + str(e) + bstack1ll1ll1_opy_ (u"ࠧࠨᅛ"))