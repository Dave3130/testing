# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11lll1_opy_, bstack11l11llll1l_opy_, bstack11l1l111l1l_opy_
import tempfile
import json
bstack11111ll1lll_opy_ = os.getenv(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧẝ"), None) or os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢẞ"))
bstack11111ll1l1l_opy_ = os.path.join(bstack11l1l11_opy_ (u"ࠨ࡬ࡰࡩࠥẟ"), bstack11l1l11_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫẠ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l1l11_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫạ"),
      datefmt=bstack11l1l11_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧẢ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l111llll_opy_():
  bstack11111llll1l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣả"), bstack11l1l11_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥẤ"))
  return logging.DEBUG if bstack11111llll1l_opy_.lower() == bstack11l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥấ") else logging.INFO
def bstack1ll11l1llll_opy_():
  global bstack11111ll1lll_opy_
  if os.path.exists(bstack11111ll1lll_opy_):
    os.remove(bstack11111ll1lll_opy_)
  if os.path.exists(bstack11111ll1l1l_opy_):
    os.remove(bstack11111ll1l1l_opy_)
def bstack1l1ll1ll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111ll111l_opy_ = log_level
  if bstack11l1l11_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨẦ") in config and config[bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩầ")] in bstack11l11llll1l_opy_:
    bstack11111ll111l_opy_ = bstack11l11llll1l_opy_[config[bstack11l1l11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪẨ")]]
  if config.get(bstack11l1l11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫẩ"), False):
    logging.getLogger().setLevel(bstack11111ll111l_opy_)
    return bstack11111ll111l_opy_
  global bstack11111ll1lll_opy_
  bstack1l1ll1ll1_opy_()
  bstack11111ll11ll_opy_ = logging.Formatter(
    fmt=bstack11l1l11_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ẫ"),
    datefmt=bstack11l1l11_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩẫ"),
  )
  bstack11111llllll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111ll1lll_opy_)
  file_handler.setFormatter(bstack11111ll11ll_opy_)
  bstack11111llllll_opy_.setFormatter(bstack11111ll11ll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111llllll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l1l11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧẬ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111llllll_opy_.setLevel(bstack11111ll111l_opy_)
  logging.getLogger().addHandler(bstack11111llllll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111ll111l_opy_
def bstack11111lllll1_opy_(config):
  try:
    bstack11111l1llll_opy_ = set(bstack11l1l111l1l_opy_)
    bstack11111l1lll1_opy_ = bstack11l1l11_opy_ (u"࠭ࠧậ")
    with open(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪẮ")) as bstack11111ll11l1_opy_:
      bstack11111lll1l1_opy_ = bstack11111ll11l1_opy_.read()
      bstack11111l1lll1_opy_ = re.sub(bstack11l1l11_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩắ"), bstack11l1l11_opy_ (u"ࠩࠪẰ"), bstack11111lll1l1_opy_, flags=re.M)
      bstack11111l1lll1_opy_ = re.sub(
        bstack11l1l11_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭ằ") + bstack11l1l11_opy_ (u"ࠫࢁ࠭Ẳ").join(bstack11111l1llll_opy_) + bstack11l1l11_opy_ (u"ࠬ࠯࠮ࠫࠦࠪẳ"),
        bstack11l1l11_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨẴ"),
        bstack11111l1lll1_opy_, flags=re.M | re.I
      )
    def bstack1111l111111_opy_(dic):
      bstack11111ll1111_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1llll_opy_:
          bstack11111ll1111_opy_[key] = bstack11l1l11_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫẵ")
        else:
          if isinstance(value, dict):
            bstack11111ll1111_opy_[key] = bstack1111l111111_opy_(value)
          else:
            bstack11111ll1111_opy_[key] = value
      return bstack11111ll1111_opy_
    bstack11111ll1111_opy_ = bstack1111l111111_opy_(config)
    return {
      bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫẶ"): bstack11111l1lll1_opy_,
      bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬặ"): json.dumps(bstack11111ll1111_opy_)
    }
  except Exception as e:
    return {}
def bstack1111l11111l_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠪࡰࡴ࡭ࠧẸ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111lll1ll_opy_ = os.path.join(log_dir, bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬẹ"))
  if not os.path.exists(bstack11111lll1ll_opy_):
    bstack11111l1ll11_opy_ = {
      bstack11l1l11_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨẺ"): str(inipath),
      bstack11l1l11_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣẻ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭Ẽ")), bstack11l1l11_opy_ (u"ࠨࡹࠪẽ")) as bstack11111lll11l_opy_:
      bstack11111lll11l_opy_.write(json.dumps(bstack11111l1ll11_opy_))
def bstack11111ll1ll1_opy_():
  try:
    bstack11111lll1ll_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠩ࡯ࡳ࡬࠭Ế"), bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩế"))
    if os.path.exists(bstack11111lll1ll_opy_):
      with open(bstack11111lll1ll_opy_, bstack11l1l11_opy_ (u"ࠫࡷ࠭Ề")) as bstack11111lll11l_opy_:
        bstack11111l1ll1l_opy_ = json.load(bstack11111lll11l_opy_)
      return bstack11111l1ll1l_opy_.get(bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭ề"), bstack11l1l11_opy_ (u"࠭ࠧỂ")), bstack11111l1ll1l_opy_.get(bstack11l1l11_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩể"), bstack11l1l11_opy_ (u"ࠨࠩỄ"))
  except:
    pass
  return None, None
def bstack1111l1111l1_opy_():
  try:
    bstack11111lll1ll_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠩ࡯ࡳ࡬࠭ễ"), bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩỆ"))
    if os.path.exists(bstack11111lll1ll_opy_):
      os.remove(bstack11111lll1ll_opy_)
  except:
    pass
def bstack1l1l1111_opy_(config):
  try:
    from bstack_utils.helper import bstack111111ll_opy_, bstack111ll1l1ll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111ll1lll_opy_
    if config.get(bstack11l1l11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ệ"), False):
      return
    uuid = os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪỈ")) if os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỉ")) else bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤỊ"))
    if not uuid or uuid == bstack11l1l11_opy_ (u"ࠨࡰࡸࡰࡱ࠭ị"):
      return
    bstack11111lll111_opy_ = [bstack11l1l11_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬỌ"), bstack11l1l11_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫọ"), bstack11l1l11_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬỎ"), bstack11111ll1lll_opy_, bstack11111ll1l1l_opy_]
    bstack11111ll1l11_opy_, root_path = bstack11111ll1ll1_opy_()
    if bstack11111ll1l11_opy_ != None:
      bstack11111lll111_opy_.append(bstack11111ll1l11_opy_)
    if root_path != None:
      bstack11111lll111_opy_.append(os.path.join(root_path, bstack11l1l11_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪỏ")))
    bstack1l1ll1ll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬỐ") + uuid + bstack11l1l11_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨố"))
    with tarfile.open(output_file, bstack11l1l11_opy_ (u"ࠣࡹ࠽࡫ࡿࠨỒ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111lll111_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111lllll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1l1ll_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1l1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1l1ll_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l1l11_opy_ (u"ࠩࡧࡥࡹࡧࠧồ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l1l11_opy_ (u"ࠪࡶࡧ࠭Ổ")), bstack11l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩổ")),
        bstack11l1l11_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧỖ"): uuid
      }
    )
    bstack11111llll11_opy_ = bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠨࡡࡱ࡫ࡶࠦỗ"), bstack11l1l11_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢỘ"), bstack11l1l11_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࠣộ")], bstack11l1l11lll1_opy_)
    response = requests.post(
      bstack11l1l11_opy_ (u"ࠤࡾࢁ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥỚ").format(bstack11111llll11_opy_),
      data=multipart_data,
      headers={bstack11l1l11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩớ"): multipart_data.content_type},
      auth=(config[bstack11l1l11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ờ")], config[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨờ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬỞ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l1l11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭ở") + str(e))
  finally:
    try:
      bstack1ll11l1llll_opy_()
      bstack1111l1111l1_opy_()
    except:
      pass